from fastapi import APIRouter, Query
from utils.summarize import summarize_log
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def summarize(filename: str = Query(...)):
    summary = summarize_log(filename)
    return JSONResponse(content={"summary": summary})

