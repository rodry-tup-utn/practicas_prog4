from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.product.router import router as product_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_router)


@app.get("/")
def heatlth():
    return {"message": "Servidor fucionando"}
