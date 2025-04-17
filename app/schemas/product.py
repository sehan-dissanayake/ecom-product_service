from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str | None = None

class Product(ProductCreate):
    id: str

    class Config:
        from_attributes = True  # Needed for compatibility with MongoDB documents