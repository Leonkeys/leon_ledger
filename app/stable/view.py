"""
月度固定消费，手动添加之后计入月度总消费中
"""
from fastapi import APIRouter
from utils.response_code import ResultResponse
from . import schema

router = APIRouter()


@router.post("/stableList",
             summary="月度固定消费列表",
             description="月度固定消费列表",
             response_model=ResultResponse[schema.StableListResponseSchema])
async def stable_list():
    return {}


@router.post("/createStable",
             summary="添加月度固定消费",
             description="添加月度固定消费",
             response_model=ResultResponse[schema.CreateStableResponseSchema])
async def add_stable():
    return {}


@router.put("/setStable",
            summary="更新固定消费列表",
            description="更新月度固定消费",
            response_model=ResultResponse[schema.SetStableResponseSchema])
async def set_stable():
    return {}


@router.post("/delStable",
             summary="删除月度固定消费",
             description="删除月度固定消费",
             response_model=ResultResponse[schema.DelStableResponseSchema])
async def del_stable():
    return {}
