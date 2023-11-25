----
# MavunoX Farming Recommendations API

## Overview

The MavunoX Farming Recommendations API provides recommendations for crop cultivation based on soil and environmental parameters.

## Endpoint

- **URL:** `https://mavunox.onrender.com/api/get_results/`
- **Method:** POST

## Request Body

### Parameters

- `R` (integer): Red component of soil color (0-255).
- `G` (integer): Green component of soil color (0-255).
- `B` (integer): Blue component of soil color (0-255).
- `temperature` (float): Temperature in degrees Celsius.
- `humidity` (float): Relative humidity in percentage.
- `label` (string): Crop label (e.g., "muskmelon").
- `country` (string): Country name (e.g., "South Africa").

### Example

```json
{
  "R": 200,
  "G": 180,
  "B": 160,
  "temperature": 27,
  "humidity": 46,
  "label": "muskmelon",
  "country": "South Africa"
}
```

## Response

The API returns a JSON object containing the following recommendations:

- `temperature` (float): Current temperature.
- `humidity` (float): Current humidity.
- `ph` (float): Soil pH value.
- `water_availability` (float): Water availability in millimeters.
- `planting_season` (string): Recommended planting season.
- `label` (string): Crop label.
- `Country` (string): Country name.
- `harvest_season` (string): Recommended harvest season.
- `exp_temperature` (object): Expected temperature range and optimum.
- `exp_humidity` (object): Expected humidity range and optimum.
- `exp_ph` (object): Expected pH range and optimum.
- `exp_water_availability` (object): Expected water availability range and optimum.
- `duration_factor` (float): Duration factor.
- `temperature_rec` (object): Temperature recommendation details.
- `humidity_rec` (object): Humidity recommendation details.
- `ph_rec` (object): pH recommendation details.
- `water_availability_rec` (object): Water availability recommendation details.
- `status` (boolean): Indicate if factors is within range, 0(Not in optimal range), 1(within optimal range).
- `scale` (object): Degree of Optimality (Closeness to optimal value in percent).
### Example

```json
{
  "temperature": 27.0,
  "humidity": 46.0,
  "ph": 7.5096330642700195,
  "water_availability": 94.2563817980022,
  "planting_season": "summer",
  "label": "muskmelon",
  "Country": "South Africa",
  "harvest_season": "rainy",
  "exp_temperature": {
    "min": 27.959327675,
    "max": 29.370037680000003,
    "opt": 28.663065755999995
  },
  "exp_humidity": {
    "min": 90.96236271000001,
    "max": 93.79355208,
    "opt": 92.34280196090002
  },
  "exp_ph": {
    "min": 6.155965203,
    "max": 6.55022227575,
    "opt": 6.358805451789998
  },
  "exp_water_availability": {
    "min": 22.0679763825,
    "max": 26.86160111,
    "opt": 24.689952066
  },
  "duration_factor": 1.0,
  "temperature_rec": {
    "status": 0,
    "scale": 89.52685871517878
  },
  "humidity_rec": {
    "status": 0,
    "scale": 3.9895851202461
  },
  "ph_rec": {
    "status": 0,
    "scale": 45.17426967622115
  },
  "water_availability_rec": {
    "status": 0,
    "scale": 29.8235440264526
  }
}
```

---




## API Endpoint: `/api/recommedations/temperature` (POST)

### Description
This endpoint provides recommendations based on temperature values for optimizing rice yield. It evaluates whether the input temperature falls within the recommended range and suggests additional practices for enhancing rice production.

### Endpoint URL
```plaintext
https://mavunox.onrender.com/api/recommedations/temperature
```

### Method
`POST`

### Input
The input should be a JSON object with the following parameters:

- `min` (float): Minimum recommended temperature.
- `max` (float): Maximum recommended temperature.
- `value` (float): Current temperature value.
- `label` (string): The label or type of crop (e.g., "rice").

Example:
```json
{
  "min": 10.0,
  "max": 30.0,
  "value": 20.0,
  "label": "rice"
}
```

### Output
The output is a string providing information about the current temperature's alignment with the recommended range and suggestions for optimizing rice yield.

Example:
```plaintext
"The current temperature of 20.0 °C falls within the recommended range of 10.0-30.0 °C for optimal rice yield. To further enhance the yield, farmers can consider practices such as proper irrigation management, nutrient supplementation, and timely pest control. It is crucial to monitor and maintain the temperature within the recommended range to support maximum rice production."
```

### Response Codes
- `200 OK`: Successful request and recommendation provided.
- `400 Bad Request`: Invalid input parameters.
- `500 Internal Server Error`: Server error.

### Notes
- Ensure that the input values are valid float numbers.
- Check the response code and handle errors accordingly.




## API Endpoint: `/api/recommedations/humidity` (POST)

### Description
This endpoint provides recommendations based on humidity values for optimizing rice yield. It evaluates whether the input humidity level falls within the recommended range and suggests additional practices for enhancing rice production.

### Endpoint URL
```plaintext
https://mavunox.onrender.com/api/recommedations/humidity
```

### Method
`POST`

### Input
The input should be a JSON object with the following parameters:

- `min` (float): Minimum recommended humidity level.
- `max` (float): Maximum recommended humidity level.
- `value` (float): Current humidity level.
- `label` (string): The label or type of crop (e.g., "rice").

Example:
```json
{
  "min": 20.0,
  "max": 30.0,
  "value": 40.0,
  "label": "rice"
}
```

### Output
The output is a string providing information about the current humidity level's alignment with the recommended range and suggestions for optimizing rice yield.

Example:
```plaintext
"The current humidity of 40.0% is higher than the recommended range for optimal rice yield (20.0-30.0%). High humidity may lead to disease outbreaks and decrease crop productivity. To improve yield, farmers should consider using proper drainage systems, ensuring good air circulation, implementing effective irrigation techniques, and adjusting planting dates to avoid peak humidity periods."
```

### Response Codes
- `200 OK`: Successful request and recommendation provided.
- `400 Bad Request`: Invalid input parameters.
- `500 Internal Server Error`: Server error.

### Notes
- Ensure that the input values are valid float numbers.
- Check the response code and handle errors accordingly.



## API Endpoint: `/api/recommedations/ph` (POST)

### Description
This endpoint provides recommendations based on pH values for optimizing rice yield. It evaluates whether the input pH level falls within the recommended range and suggests additional practices for enhancing rice production.

### Endpoint URL
```plaintext
https://mavunox.onrender.com/api/recommedations/ph
```

### Method
`POST`

### Input
The input should be a JSON object with the following parameters:

- `min` (float): Minimum recommended pH level.
- `max` (float): Maximum recommended pH level.
- `value` (float): Current pH level.
- `label` (string): The label or type of crop (e.g., "rice").

Example:
```json
{
  "min": 7.0,
  "max": 8.0,
  "value": 4.0,
  "label": "rice"
}
```

### Output
The output is a string providing information about the current pH level's suitability for optimal rice yield and suggestions for adjustment.

Example:
```plaintext
"The current pH level of 4.0 is not suitable for optimal rice yield. To improve yield, raise the pH to 7.0-8.0. Lime application is recommended for acid soils. Apply approximately 6.67 kg of agricultural lime per 10 m². It's important to test soil pH regularly and adjust lime application accordingly to maintain optimal pH levels for maximum rice production."
```

### Response Codes
- `200 OK`: Successful request and recommendation provided.
- `400 Bad Request`: Invalid input parameters.
- `500 Internal Server Error`: Server error.

### Notes
- Ensure that the input values are valid float numbers.
- Check the response code and handle errors accordingly.



## API Endpoint: `/api/recommedations/water_availability` (POST)

### Description
This endpoint provides recommendations based on water availability values for optimizing rice yield. It evaluates whether the input water availability falls within the recommended range and suggests additional practices for enhancing rice production.

### Endpoint URL
```plaintext
https://mavunox.onrender.com/api/recommedations/water_availability
```

### Method
`POST`

### Input
The input should be a JSON object with the following parameters:

- `min` (float): Minimum recommended water availability.
- `max` (float): Maximum recommended water availability.
- `value` (float): Current water availability.
- `label` (string): The label or type of crop (e.g., "rice").

Example:
```json
{
  "min": 150.0,
  "max": 170.0,
  "value": 160.0,
  "label": "rice"
}
```

### Output
The output is a string providing information about the current water availability and its alignment with the recommended range, along with suggestions for optimizing rice yield.

Example:
```plaintext
"Based on the current water availability of 160.0 mm, it falls within the recommended range of 150.0-170.0 mm for optimal yield. To further improve rice yield, consider proper irrigation management with a focus on avoiding water stress during critical growth stages. Additionally, implementing water-saving techniques such as drip irrigation and mulching can help conserve water and enhance overall crop productivity."
```

### Response Codes
- `200 OK`: Successful request and recommendation provided.
- `400 Bad Request`: Invalid input parameters.
- `500 Internal Server Error`: Server error.

### Notes
- Ensure that the input values are valid float numbers.
- Check the response code and handle errors accordingly.

Feel free to tailor the documentation to fit your specific documentation style or requirements.