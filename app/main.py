from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import client
from app.database import initialize_database
from app.routers.product import router as product_router 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await initialize_database()
    print("Connected to MongoDB!")
    yield
    # Shutdown code
    client.close()
    print("Disconnected from MongoDB!")

app = FastAPI(lifespan=lifespan)

app.include_router(product_router)

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
