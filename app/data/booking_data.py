from typing import Optional
from app.models.booking_model import Booking

booking_data = []

def create_booking(new_booking: Booking):
    booking_data.append(new_booking)
    return new_booking

def get_booking_by_id(booking_id: int) -> Optional[Booking]:
    for booking in booking_data:
        if booking.id == booking_id:
            return booking
    return None

def update_booking_by_id(booking_id: int, updated_booking: Booking) -> Optional[Booking]:
    booking = get_booking_by_id(booking_id)
    if booking:
        booking.customer_name = updated_booking.customer_name
        booking.flight_id = updated_booking.flight_id
        return booking

def delete_booking(booking_id: int) -> bool:
    for booking in booking_data:
        if booking.id == booking_id:
            booking_data.remove(booking)
            return True
    return False