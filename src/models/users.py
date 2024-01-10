import uuid
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True
        
        json_schema_extra = {
            "example": {
                "_id": "60f7b2e8e6b3f9f9f9f9f9f9",
                "name": "John Doe",
                "email": "minhphi@gmail.com",
                "password": "123456"
                }
            }

class UserUpdate(BaseModel):
    name: Optional[str] 
    email: Optional[str]
    password: Optional[str] 

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "minhphi@gmail.com",
                "password": "123456"
                }
            }

