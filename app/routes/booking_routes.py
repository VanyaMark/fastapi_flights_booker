from fastapi import APIRouter, HTTPException
from typing import List
from app.models.booking_model import Booking
from app.data.booking_data import booking_data, create_booking, get_booking_by_id, update_booking_by_id, delete_booking

router = APIRouter()

@router.get("/bookings", response_model=List[Booking])
async def get_bookings():
    return booking_data

@router.post("/bookings", response_model=Booking)
async def create_new_booking(booking: Booking):
    return create_booking(booking)

@router.get("/bookings/{booking_id}", response_model=Booking)
async def get_booking(booking_id: int):
    booking = get_booking_by_id(booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.put("/bookings/{booking_id}", response_model=Booking)
async def update_existing_booking(booking_id: int, booking: Booking):
    updated_booking = update_booking_by_id(booking_id, booking)
    if updated_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated_booking

@router.delete("/bookings/{booking_id}", status_code=204)
async def delete_existing_booking(booking_id: int):
    if delete_booking(booking_id):
        return
    raise HTTPException(status_code=404, detail="Booking not found")