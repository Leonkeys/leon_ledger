from typing import List
from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/list")
def lis():
    return {"hello": "hello"}
