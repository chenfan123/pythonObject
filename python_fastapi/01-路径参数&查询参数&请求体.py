# 第一个fastapi程序
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()  # 创建一个FastAPI实例


@app.get("/args1/1")
def path_args1():
    return {"message": "id1"}


# 路径参数
@app.get("/args1/{id}")
def path_args2(id: int):
    return {"message": f"id: {id}"}

# 查询参数


@app.get("/query1")
def page_limit(page, limit):
    return {"page": page, "limit": limit}


@app.get("/query2")
def page_limit(page: int = 1, limit: int = 10):
    return {"page": page, "limit": limit}

# 请求体


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
