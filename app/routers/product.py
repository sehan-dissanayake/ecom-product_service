from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate, Product as ProductSchema

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductSchema)
async def create_product(product: ProductCreate):
    new_product = Product(**product.model_dump())
    await new_product.insert()
    return new_product