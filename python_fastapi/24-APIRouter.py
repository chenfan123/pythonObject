from fastapi import FastAPI
from fastapi.routing import APIRouter

app = FastAPI()

main_router = APIRouter(tags=["main"], prefix="/main")
user_router = APIRouter(tags=["user"], prefix="/user")
item_router = APIRouter(tags=["item"], prefix="/item")


@main_router.get("/info")
async def get_info():
    return {"message": "main: info1"}


@user_router.get("/info")
async def get_info():
    return {"message": "user: info2"}


@item_router.get("/info")
async def get_info():
    return {"message": "item: info2"}

app.include_router(main_router)  # 将main_router注册到app中
app.include_router(user_router)  # 将user_router注册到app中
app.include_router(item_router)  # 将item_router注册到app中

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
