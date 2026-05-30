from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.product.router import router as product_router
from app.modules.category.router import router as category_router
from contextlib import asynccontextmanager
from app.core.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_router)
app.include_router(category_router)


@app.get("/")
def heatlth():
    return {"message": "Servidor fucionando"}
