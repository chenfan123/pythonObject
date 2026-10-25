# 第一个fastapi程序
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Union, Optional  # 联合类型,可选类型
from typing import Literal  # 字面量类型

app = FastAPI()  # 创建一个FastAPI实例


@app.get("/args1/1")
def path_args1():
    return {"message": "id1"}


@app.get("/args1/{id}")
def path_args2(id: int):
    return {"message": f"id: {id}"}


@app.get("/args2/{id}")
def path_args2(id: Union[int, str]):  # 可以是int也可以是str
    return {"message": f"id: {id}"}


@app.get("/args3/{type}")
def path_args3(type: Optional[Literal["1", "2"]] = None):  # 可选类型,默认值为None
    return {"message": f"type: {type}"}


@app.get("/query1")
def page_limit(page: int = 1, limit: Union[int, str] = 10):  # 默认值为10
    return {"page": page, "limit": limit}


@app.get("/query2")
def page_limit(page: int = 1, limit: int = 10):
    return {"page": page, "limit": limit}


class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/body")
def body(user: User):
    return {"user": user}


if __name__ == "__main__":
    # 传入 app 对象时不能开 reload，否则 uvicorn 会直接退出。
    # 需要改代码自动重启时，在本目录执行：fastapi dev "01-路径参数.py"
    uvicorn.run(app, host="0.0.0.0", port=8000)
