from typing import Optional
from app.models.flight_model import Flight

flight_data = [
    Flight(id=1, airline="Delta", origin="JFK", destination="LAX", departure_time="2024-10-15T08:00", arrival_time="2024-10-15T11:00", price=295.00),
    Flight(id=2, airline="American", origin="JFK", destination="LAX", departure_time="2024-10-15T12:00", arrival_time="2024-10-15T20:00", price=310.00),
    Flight(id=3, airline="United", origin="JFK", destination="LAX", departure_time="2024-10-15T06:30", arrival_time="2024-10-15T09:00", price=270.00),
    Flight(id=4, airline="JetBlue", origin="JFK", destination="LAX", departure_time="2024-10-15T09:00", arrival_time="2024-10-15T12:00", price=300.00),
    Flight(id=5, airline="Delta", origin="JFK", destination="LAX", departure_time="2024-10-15T10:00", arrival_time="2024-10-15T13:00", price=280.00),
    Flight(id=6, airline="American", origin="JFK", destination="LAX", departure_time="2024-10-15T11:30", arrival_time="2024-10-15T15:00", price=325.00),
    Flight(id=7, airline="Alaska", origin="JFK", destination="LAX", departure_time="2024-10-15T13:00", arrival_time="2024-10-15T16:30", price=335.00),
    Flight(id=8, airline="Southwest", origin="JFK", destination="LAX", departure_time="2024-10-15T14:00", arrival_time="2024-10-15T17:00", price=300.00),
    Flight(id=9, airline="United", origin="JFK", destination="LAX", departure_time="2024-10-15T15:00", arrival_time="2024-10-15T18:00", price=310.00),
    Flight(id=10, airline="JetBlue", origin="JFK", destination="LAX", departure_time="2024-10-15T16:00", arrival_time="2024-10-15T19:00", price=320.00),
    Flight(id=11, airline="Delta", origin="JFK", destination="LAX", departure_time="2024-10-15T17:00", arrival_time="2024-10-15T20:00", price=340.00),
    Flight(id=12, airline="American", origin="JFK", destination="LAX", departure_time="2024-10-15T18:00", arrival_time="2024-10-15T21:00", price=330.00),
]

def get_flight_by_id(flight_id: int) -> Optional[Flight]:
    for flight in flight_data:
        if flight.id == flight_id:
            return flight
    return None