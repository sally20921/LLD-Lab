# api/routes/run.py

from fastapi import APIRouter
from pydantic import BaseModel
from core.lldm_runner import run_experiment

router = APIRouter()

class RunRequest(BaseModel):
    prompt: str
    model: str  # "llada" or "dream7b"
    steps: int = 10

@router.post("/")
def run_experiment_api(req: RunRequest):
    result = run_experiment(req.prompt, req.model, req.steps)
    return result

