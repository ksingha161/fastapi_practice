from fastapi import FastAPI
import psycopg2
from . import models
from .database import engine, get_db
from .routers import product, user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(
    product.router, 
    prefix="/products",
    tags=['Products']
    )

app.include_router(
    user.router, 
    prefix="/user",
    tags=['Users']
    )

app.include_router(
    auth.router, 
    prefix="/login",
    tags=['Authorization']
    )

@app.get("/")
def get_home_page():
    return {"message": "welcome to products API"}
