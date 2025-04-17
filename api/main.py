# api/main.py

from fastapi import FastAPI
from api.routes import run

app = FastAPI()
app.include_router(run.router, prefix="/run")

@app.get("/")
def health_check():
    return {"status": "LLD-Lab running"}

