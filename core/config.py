from typing import Optional, List, Dict
from pathlib import Path


class APISettings:
    # 开发模式配置
    DEBUG: bool = False
    TITLE: str = "leon_bill"

    DESCRIPTION: str = "大型项目框架"
    # 文档地址 默认为docs
    DOCS_URL: str = "/openapi/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/openapi/redoc"
    # 项目根路径
    BASE_PATH: Path = Path(__file__).resolve().parent.parent



settings = APISettings()
