
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#3-a
@app.get("/ping")
async def ping():
    return "pong"

#3-b
class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

sauvegarde_cars = []

@app.post("/cars", status_code=201)
async def post_car(car: Car):
    sauvegarde_cars.append(car)
    return car

#3-c
@app.get("/cars", response_model=List[Car])
async def recupere_cars():
    return sauvegarde_cars

#3-d
@app.get("/cars/{id}")
async def get_car(id: str):
    for car in sauvegarde_cars:
        if car.identifier == id:
            return car
    raise HTTPException(status_code=404, detail=f"Car with id {id} not found")


#3-e
@app.put("/cars/{id}/characteristics")
async def update_car_characteristics(id: str, characteristics: Characteristic):
    for car in sauvegarde_cars:
        if car.identifier == id:
            car.characteristics = characteristics
            return car
    raise HTTPException(status_code=404, detail=f"Car with id {id} not found")