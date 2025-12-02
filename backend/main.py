# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings
from routes import convert

class Settings(BaseSettings):
    # Variables de Backend
    DATABASE_URL: str = "sqlite:///./test.db" # Default for now
    SECRET_KEY: str = "secret"
    
    # Variables que comparte (opcional)
    VITE_API_URL: str = "http://localhost:8000"

    class Config:
        # Le decimos que el archivo está un nivel arriba
        env_file = "../.env" 
        extra = "ignore" # Ignora las variables que no estén declaradas aquí

settings = Settings()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(convert.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}