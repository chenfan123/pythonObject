# 第一个fastapi程序
from fastapi import FastAPI, Query, Form
from pydantic import BaseModel
import uvicorn
from typing import Annotated

app = FastAPI()  # 创建一个FastAPI实例


@app.post("/login")
def login(username: str = Form(..., description="用户名"), password: str = Form(..., description="密码")):
    return {"username": username, "password": password}


class User(BaseModel):
    username: str
    password: str


@app.post("/login2")
def login(user: Annotated[User, Form()]):  # 使用 Annotated 包装 Form 参数
    return {"username": user.username, "password": user.password}


class User2(BaseModel):
    username: str = Form(..., description="用户名")
    password: str = Form(..., description="密码")


@app.post("/login3")
def login(user: Annotated[User2, Form()]):
    return {"username": user.username, "password": user.password}


if __name__ == "__main__":
    # 传入 app 对象时不能开 reload，否则 uvicorn 会直接退出。
    # 需要改代码自动重启时，在本目录执行：fastapi dev "01-路径参数.py"
    uvicorn.run(app, host="0.0.0.0", port=8000)
