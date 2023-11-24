Sure, here is an example of API documentation for the provided endpoint:

---

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

