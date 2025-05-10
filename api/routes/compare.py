from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from utils.compare import compare_entropy

router = APIRouter()

@router.get("/")
def compare(filenames: list[str] = Query(...)):
    image_b64 = compare_entropy(filenames)
    return JSONResponse(content={"image_base64": image_b64})

