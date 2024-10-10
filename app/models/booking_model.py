from pydantic import BaseModel


class Booking(BaseModel):
    id: int
    customer_name: str
    flight_id: int