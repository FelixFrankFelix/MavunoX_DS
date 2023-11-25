----
# MavunoX Farming Recommendations API

## Overview

The MavunoX Farming Recommendations API provides recommendations for crop cultivation based on soil and environmental parameters.


## API Endpoint: `/api/get_first_results/` (POST)

### Description
This endpoint provides recommendations based on color values (R, G, B), label, and country for optimizing rice yield. It takes input values and returns expected values for pH, water availability, and additional information related to rice cultivation.

### Endpoint URL
```plaintext
https://mavunox.onrender.com/api/get_first_results/
```

### Method
`POST`

### Input
The input should be a JSON object with the following parameters:

- `R` (int): Red color value.
- `G` (int): Green color value.
- `B` (int): Blue color value.
- `label` (string): The label or type of crop (e.g., "rice").
- `country` (string): The country where the crop is cultivated.

Example:
```json
{
  "R": 255,
  "G": 128,
  "B": 64,
  "label": "rice",
  "country": "Nigeria"
}
```

### Output
The output is a JSON object providing expected values for pH, water availability, and additional information related to cultivation.

Example:
```json
{
  "ph": 6.880090236663818,
  "water_availability": 135.48224195338514,
  "label": "rice",
  "Country": "Nigeria",
  "harvest_season": "summer",
  "exp_ph": {
    "min": 5.580074332000001,
    "max": 7.28623774985,
    "opt": 6.425470922139999
  },
  "exp_water_availability": {
    "min": 195.01710482,
    "max": 276.851351895,
    "opt": 236.18111359399998
  },
  "duration": 140,
  "ph_rec": {
    "status": 1,
    "scale": 88.33734516996184
  },
  "water_availability_rec": {
    "status": 0,
    "scale": 7.92565129376272
  }
}
```

### Response Codes
- `200 OK`: Successful request and recommendation provided.
- `400 Bad Request`: Invalid input parameters.
- `500 Internal Server Error`: Server error.

### Output Details
- `ph`: Current pH value.
- `water_availability`: Current water availability value.
- `exp_ph`: Expected pH range with minimum (`min`), maximum (`max`), and optimal (`opt`) values.
- `exp_water_availability`: Expected water availability range with minimum (`min`), maximum (`max`), and optimal (`opt`) values.
- `duration`: Expected duration of cultivation.
- `ph_rec`: pH recommendation with `status` indicating the recommendation status (1 for success) and `scale` providing a scale value.
- `water_availability_rec`: Water availability recommendation with `status` indicating the recommendation status (1 for success) and `scale` providing a scale value.

### Notes
- Ensure that the input values are within the expected data types.
- Check the response code and handle errors accordingly.



## API Endpoint: `/api/get_second_results/` (POST)

### Description
This endpoint provides recommendations based on temperature and humidity values for optimizing rice yield. It takes input values for temperature, humidity, and the crop label and returns expected and recommended values.

### Endpoint URL
```plaintext
https://mavunox.onrender.com/api/get_second_results/
```

### Method
`POST`

### Input
The input should be a JSON object with the following parameters:

- `temperature` (float): Current temperature value.
- `humidity` (float): Current humidity level.
- `label` (string): The label or type of crop (e.g., "rice").

Example:
```json
{
  "temperature": 20,
  "humidity": 84,
  "label": "rice"
}
```

### Output
The output is a JSON object providing expected and recommended values for temperature and humidity.

Example:
```json
{
  "temperature": 20.0,
  "humidity": 84.0,
  "exp_temperature": {
    "min": 21.9270636125,
    "max": 25.51370224,
    "opt": 23.6893322105
  },
  "exp_humidity": {
    "min": 80.9520935175,
    "max": 83.47025390249999,
    "opt": 82.27282153889999
  },
  "temperature_rec": {
    "status": 0,
    "scale": 58.01625904424251
  },
  "humidity_rec": {
    "status": 0,
    "scale": 99.5535278480284
  }
}
```

### Response Codes
- `200 OK`: Successful request and recommendation provided.
- `400 Bad Request`: Invalid input parameters.
- `500 Internal Server Error`: Server error.

### Output Details
- `exp_temperature`: Expected temperature range with minimum (`min`), maximum (`max`), and optimal (`opt`) values.
- `exp_humidity`: Expected humidity range with minimum (`min`), maximum (`max`), and optimal (`opt`) values.
- `temperature_rec`: Temperature recommendation with `status` indicating the recommendation status (1 for success) and `scale` providing a scale value.
- `humidity_rec`: Humidity recommendation with `status` indicating the recommendation status (1 for success) and `scale` providing a scale value.

### Notes
- Ensure that the input values are valid float numbers.
- Check the response code and handle errors accordingly.

Feel free to customize the documentation based on your specific API documentation format or requirements.

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

