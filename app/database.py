from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.product import Product
from fastapi import FastAPI
from contextlib import asynccontextmanager

MONGO_DETAILS = "mongodb://root:password@localhost:27018"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.product_db

def get_database():
    return database

async def initialize_database():
    await init_beanie(
        database=database,
        document_models=[Product]
    )
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await initialize_database()
    print("Connected to MongoDB!")
    yield
    # Shutdown code
    client.close()
    print("Disconnected from MongoDB!")    