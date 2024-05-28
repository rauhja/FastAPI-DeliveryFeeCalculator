from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

from .feecalculator import FeeCalculator


class FeeRequest(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime

    @validator("cart_value", "delivery_distance", "number_of_items")
    def check_positive_value(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Value must be positive")
        return value


class FeeResponse(BaseModel):
    delivery_fee: int


app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}


@app.post("/calculate_delivery_fee", response_model=FeeResponse)
def calculate_delivery_fee(request: FeeRequest) -> FeeResponse:
    try:
        fee_calculator = FeeCalculator(
            request.cart_value,
            request.delivery_distance,
            request.number_of_items,
            request.time,
        )
        return FeeResponse(delivery_fee=fee_calculator.get_delivery_fee())

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error") from None
