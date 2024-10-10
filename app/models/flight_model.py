from pydantic import BaseModel

class Flight(BaseModel):
    id: int
    airline: str
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    price: float
