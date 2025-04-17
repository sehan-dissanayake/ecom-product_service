from fastapi import FastAPI
from app.routers.product import router as product_router 
from app.database import lifespan as db_lifespan

app = FastAPI(lifespan=db_lifespan)

app.include_router(product_router)

@app.get("/health")
async def health_check():
    return {"status": "OK"}