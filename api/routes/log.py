from fastapi import APIRouter
from utils.logging import list_logs, read_log

router = APIRouter()

@router.get("/list")
def get_log_list():
    return list_logs()

@router.get("/view")
def view_log(filename: str):
    return read_log(filename)

