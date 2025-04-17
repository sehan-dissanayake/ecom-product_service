from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from beanie import PydanticObjectId

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=Product)
async def create_product(product: ProductCreate):
    new_product = Product(**product.model_dump())
    await new_product.insert()
    return new_product

@router.get("/", response_model=list[Product])
async def get_all_products():
    products = await Product.find_all().to_list()
    return products

@router.get("/{id}", response_model=Product)
async def get_product(id: PydanticObjectId):
    product = await Product.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{id}", response_model=Product)
async def update_product(id: PydanticObjectId, product_data: ProductCreate):
    product = await Product.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Update fields
    product.name = product_data.name
    product.price = product_data.price
    product.description = product_data.description
    
    await product.save()  # Beanie's save method
    return product

@router.delete("/{id}")
async def delete_product(id: PydanticObjectId):
    product = await Product.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    await product.delete()  # Beanie's delete method
    return {"message": "Product deleted successfully"}

@router.patch("/{id}", response_model=Product)
async def partial_update_product(
    id: PydanticObjectId, 
    product_data: ProductUpdate
):
    product = await Product.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Update only provided fields
    update_data = product_data.model_dump(exclude_unset=True)
    await product.update({"$set": update_data})
    return await Product.get(id)