from typing import Optional
from beanie import Document  

class Product(Document):
    name: str
    price: float
    description: Optional[str] = None

    class Settings:
        name = "products"  # MongoDB collection name

    class Config:
        json_schema_extra  = {
            "example": {
                "name": "Wireless Mouse",
                "price": 29.99,
                "description": "Ergonomic wireless mouse"
            }
        }