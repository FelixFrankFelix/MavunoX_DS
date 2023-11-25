import pickle
#from catboost import CatBoostClassifier
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import colorsys
import json
import math
import recommendation_engine as rec

# Load main_model model
main_model_path = 'ML_Models/main_model_xgboost.pkl'
with open(main_model_path, 'rb') as main_model_file:
    model = pickle.load(main_model_file)

# Load soil_model model
soil_model_path = 'ML_Models/soil_colour_model.pkl'
with open(soil_model_path, 'rb') as soil_model_file:
    soil_model = pickle.load(soil_model_file)

# Load label encoder
label_encoder_path = 'ML_Models/label_encoder.pkl'
with open(label_encoder_path, 'rb') as label_encoder_file:
    label_encoder = pickle.load(label_encoder_file)

# Load one-hot encoder information
one_hot_encoder_info_path = 'ML_Models/one_hot_encoder_info.pkl'
with open(one_hot_encoder_info_path, 'rb') as one_hot_encoder_info_file:
    one_hot_encoder_info = pickle.load(one_hot_encoder_info_file)

# Load crop info
crop_info_path = 'ML_Models/crop_info.pkl'
with open(crop_info_path, 'rb') as crop_info_file:
    crop_info = pickle.load(crop_info_file)


duration_factor = {
    'blackgram': 1,
    'chickpea': 1,
    'cotton': 3,
    'jute': 2,
    'kidneybeans': 1,
    'lentil': 2,
    'maize': 1,
    'mothbeans': 1,
    'mungbean': 2,
    'muskmelon': 1,
    'pigeonpeas': 3,
    'rice': 3,
    'watermelon': 1
}
#print(crop_info['rice']['ph']['max'])




def get_SoilProfile(R,G,B):
    rgb = {
        'R' : R,
        'G' : G,
        'B' : B
    }
    rgb_data = pd.DataFrame.from_dict({0: rgb}, orient='index')
    rgb_data['R/G'] = rgb_data['R']/rgb_data['G']
    rgb_data['G/B'] = rgb_data['G']/rgb_data['B']
    rgb_data['R/B'] = rgb_data['R']/rgb_data['B']

    def rgb_to_hue(rgb):
        rgb = rgb / 255.0
        max_rgb = rgb.max(axis=1)
        min_rgb = rgb.min(axis=1)
        delta = max_rgb - min_rgb
        hue = np.zeros_like(max_rgb)
        non_zero_delta = delta != 0
        hue[non_zero_delta] = np.select(
            [max_rgb == rgb[:, 0], max_rgb == rgb[:, 1], max_rgb == rgb[:, 2]],
            [
                (rgb[:, 1] - rgb[:, 2]) / delta,
                2 + (rgb[:, 2] - rgb[:, 0]) / delta,
                4 + (rgb[:, 0] - rgb[:, 1]) / delta
            ]
        )
        hue = (hue * 60) % 360
        return hue



    # Apply the function to create a new 'hue' column
    rgb_data['hue'] = rgb_to_hue(rgb_data[['R', 'G', 'B']].values)

    # Assuming df is your DataFrame with columns 'R', 'G', 'B'
    # Add new columns for Saturation, Brightness, Opacity, and Temperature
    rgb_data['Saturation'] = rgb_data.apply(lambda row: colorsys.rgb_to_hsv(row['R']/255, row['G']/255, row['B']/255)[1], axis=1)
    rgb_data['Brightness'] = rgb_data.apply(lambda row: colorsys.rgb_to_hsv(row['R']/255, row['G']/255, row['B']/255)[2], axis=1)


    soil_pH = soil_model.predict(rgb_data)[0]

    gray_scale = 1- ((R*0.299 + G*0.582 + B*0.114)/255)
    
    # Ensure x is within the range [x1, x2

    # Linear interpolation formula
    water_availabiliy = 25 + ((gray_scale - 0.12) * (250 - 25)) / (0.65 - 0.12)
    return soil_pH,water_availabiliy


def get_HarvestSeason(temperature,humidity,soil_pH,water_availability,label,country):
    new_entry = {
        'ph': soil_pH,
        'water_availability': water_availability,
        'label': label,
        'Country': country
    }
   
    # Convert the single-entry dictionary to a DataFrame
    new_data = pd.DataFrame.from_dict({0: new_entry}, orient='index')
    # Apply the same one-hot encoding to 'Country' and 'label'
    new_data_encoded = pd.get_dummies(new_data, columns=['Country', 'label'], dtype=int)
    new_data_encoded['humidity_to_temperature_ratio'] = new_data_encoded['humidity'] / new_data_encoded['temperature']
    new_data_encoded['ph_to_water_availability_ratio'] = new_data_encoded['ph'] / new_data_encoded['water_availability']

    # Ensure the columns match the ones used during training
    new_data_encoded = new_data_encoded.reindex(columns=one_hot_encoder_info['columns'], fill_value=0)

    new_data_encoded = new_data_encoded.drop('season',axis = 1)
    # Make predictions with the XGBoost model
    predictions = model.predict(new_data_encoded)
    # Inverse transform the predicted labels to get harvest season in words
    predictions_words = label_encoder.inverse_transform(predictions)
    # Print the predicted harvest season
   
    Harvest_season = predictions_words[0]
    return Harvest_season



#soil_pH,water_avail = get_SoilProfile(entry['RGB'][0],entry['RGB'][1],entry['RGB'][2])

#print(get_HarvestSeason(23,15,7,200,'rice','Nigeria'))
#harvest_season = get_HarvestSeason(entry['temperature'], entry['humidity'],soil_pH,water_avail,entry['label'],entry['country'])

def calc_status(value, value_range):
    if value >= value_range[0] and value <= value_range[1] :
        status = 1
    else: status = 0
    return status


def calc_scale(actual_number, input_number, k):
    absolute_difference = abs(actual_number - input_number)
    scale_value = 100 * math.exp(-k * absolute_difference**2)
    return scale_value



#print(calc_scale(14, 68, 0.0003))

#for i in range(5,9,1):
#    print(i, calc_scale(i, 6.5, 0.6))

#print(crop_info)

#print(soil_pH,water_avail,harvest_season)
def get_First_Results(entry):
    global soil_pH, water_avail
    soil_pH, water_avail = get_SoilProfile(entry.R, entry.G, entry.B)
    harvest_season = get_HarvestSeason(soil_pH, water_avail, entry.label, entry.country)

    ph_status = calc_status(soil_pH, [crop_info[entry.label]['ph']['min'], crop_info[entry.label]['ph']['max']])
    water_availability_status = calc_status(water_avail, [crop_info[entry.label]['water availability']['min'], crop_info[entry.label]['water availability']['max']])

    
    ph_scale = calc_scale(soil_pH, crop_info[entry.label]['ph']['opt'], 0.6)
    water_availability_scale = calc_scale(water_avail, crop_info[entry.label]['water availability']['opt'], 0.00025)

    results = {
        'ph': float(soil_pH),
        'water_availability': float(water_avail),
        'label': entry.label,
        'Country': entry.country,
        'harvest_season': harvest_season,
        
        'exp_ph': {
            'min': float(crop_info[entry.label]['ph']['min']),
            'max': float(crop_info[entry.label]['ph']['max']),
            'opt': float(crop_info[entry.label]['ph']['opt']),
        },
        'exp_water_availability': {
            'min': float(crop_info[entry.label]['water availability']['min']),
            'max': float(crop_info[entry.label]['water availability']['max']),
            'opt': float(crop_info[entry.label]['water availability']['opt']),
        },
        'duration_factor': float(duration_factor[entry.label]),
        
        'ph_rec': {
            'status': int(ph_status),
            'scale': float(ph_scale)
        },
        'water_availability_rec': {
            'status': int(water_availability_status),
            'scale': float(water_availability_scale)
        },
    }

    return results

def get_Second_Results(entry):
    temperature_status = calc_status(entry.temperature, [crop_info[entry.label]['temperature']['min'], crop_info[entry.label]['temperature']['max']])
    humidity_status = calc_status(entry.humidity, [crop_info[entry.label]['humidity']['min'], crop_info[entry.label]['humidity']['max']])
    temperature_scale = calc_scale(entry.temperature, crop_info[entry.label]['temperature']['opt'], 0.04)
    humidity_scale = calc_scale(entry.humidity, crop_info[entry.label]['humidity']['opt'], 0.0015)
    
    results = {
        'temperature': float(entry.temperature),
        'humidity': float(entry.humidity),
        'exp_temperature': {
            'min': float(crop_info[entry.label]['temperature']['min']),
            'max': float(crop_info[entry.label]['temperature']['max']),
            'opt': float(crop_info[entry.label]['temperature']['opt']),
        },
        'exp_humidity': {
            'min': float(crop_info[entry.label]['humidity']['min']),
            'max': float(crop_info[entry.label]['humidity']['max']),
            'opt': float(crop_info[entry.label]['humidity']['opt']),
        },
        'temperature_rec': {
            'status':int(temperature_status),
            'scale': float(temperature_scale)
        },
        'humidity_rec': {
            'status': int(humidity_status),
            'scale': float(humidity_scale)
        },
    }
    return results

#print(get_Results(entry))
