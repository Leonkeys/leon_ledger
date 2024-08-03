from fastapi import FastAPI
from .router import api_router
from .config import settings


def create_app() -> FastAPI:
    """
    生成FatAPI对象
    :return:
    """
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL,
        # dependencies=[Depends(OAuth2CustomJwt(tokenUrl="/auth/login"))]
    )

    # 跨域设置
    # register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    # register_exception(app)

    # 请求拦截
    # register_hook(app)

    # 取消挂载在 request对象上面的操作，感觉特别麻烦，直接使用全局的
    # register_init(app)
    return app


def register_router(app: FastAPI) -> None:
    """
    注册路由
    :param app:
    :return:
    """
    # 项目API
    app.include_router(api_router)

# def register_cors(app: FastAPI) -> None:
#     """
#     支持跨域
#     :param app:
#     :return:
#     """
#
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
