from pydantic import BaseModel, validator
from datetime import datetime

class OrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: datetime
    status: str
    complete: bool

    @validator('status')
    def status_must_be_valid(cls, v):
        valid_statuses = ['placed', 'approved', 'delivered']
        if v not in valid_statuses:
            raise ValueError(f'Status must be one of: {", ".join(valid_statuses)}')
        return v

class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int
