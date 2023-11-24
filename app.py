import general as gn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import recommendation_engine as rec
app = FastAPI()

class CropData(BaseModel):
    R: int
    G: int
    B:int
    temperature: float
    humidity: float
    label: str
    country: str

class FarmData(BaseModel):
    min : float
    max : float
    value: float
    label: str

@app.post("/api/recommedations/temperature")
def rec_gen(data: FarmData):
    recommedation= rec.rec_gen('temperature',data.min,data.max,data.value,'°C',data.label)
    return recommedation

@app.post("/api/recommedations/humidity")
def rec_gen(data: FarmData):
    recommedation= rec.rec_gen('humidity',data.min,data.max,data.value,'%',data.label)
    return recommedation

@app.post("/api/recommedations/ph")
def rec_gen(data: FarmData):
    recommedation= rec.rec_gen('ph',data.min,data.max,data.value,'',data.label)
    return recommedation

@app.post("/api/recommedations/water_availability")
def rec_gen(data: FarmData):
    recommedation= rec.rec_gen('water availability',data.min,data.max,data.value,'mm',data.label)
    return recommedation


@app.post("/api/get_results/")
def process_crop_data(data: CropData):
    
    results = gn.get_Results(data)
    # Perform processing or any logic with the data
    # For demonstration, just return the received data
    return results
