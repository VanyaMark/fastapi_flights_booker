from fastapi import FastAPI
from app.routes.flight_routes import router as flight_router
from app.routes.booking_routes import router as booking_router

app = FastAPI()

app.include_router(flight_router)
app.include_router(booking_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to out Flight Booking API"}