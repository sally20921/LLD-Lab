# api/main.py

from fastapi import FastAPI
from api.routes import run
from api.routes import log
from api.routes import visualize
from api.routes import summarize 
from api.routes import compare

app = FastAPI()
app.include_router(run.router, prefix="/run")
app.include_router(log.router, prefix="/log")
app.include_router(visualize.router, prefix="/visualize")
app.include_router(summarize.router, prefix="/summarize")
app.include_router(compare.router, prefix="/compare")

@app.get("/")
def health_check():
    return {"status": "LLD-Lab running"}

