from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from utils.logging import read_log
from utils.plotting import plot_entropy

router = APIRouter()

@router.get("/")
def visualize_entropy(filename: str = Query(...)):
    log = read_log(filename)
    entropy = log.get("entropy", [])
    image_b64 = plot_entropy(entropy)
    return JSONResponse(content={"image_base64": image_b64})

