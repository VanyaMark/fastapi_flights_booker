from fastapi import APIRouter, HTTPException
from typing import List
from app.data.flight_data import flight_data, get_flight_by_id
from app.models.flight_model import Flight

router = APIRouter()

@router.get("/flights", response_model=List[Flight])
async def get_flights():
    return flight_data

@router.get("/flights/{flight_id}", response_model=Flight)
async def get_flight(flight_id: int):
    flight = get_flight_by_id(flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight