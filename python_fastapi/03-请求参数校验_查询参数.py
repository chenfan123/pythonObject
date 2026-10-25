# 第一个fastapi程序
from fastapi import FastAPI, Query
import uvicorn
from pydantic import BaseModel
from typing import Union, Optional  # 联合类型,可选类型
from typing import Literal  # 字面量类型

app = FastAPI()  # 创建一个FastAPI实例


@app.get("/item1")
def page_limit(item_id=Query(default=10)):  # 默认值为10
    return {"item_id": item_id}


@app.get("/item2")
def page_limit(item_id=Query(..., description="The ID of the item")):  # 必须传递
    return {"item_id": item_id}


@app.get("/item3")
def page_limit(item_id=Query(default=10, gt=0, lt=100)):  # 默认值为10,大于0,小于100
    return {"item_id": item_id}


@app.get("/item4")
def page_limit(item_id=Query(..., deprecated=True)):  # 必须传递
    return {"item_id": item_id}


if __name__ == "__main__":
    # 传入 app 对象时不能开 reload，否则 uvicorn 会直接退出。
    # 需要改代码自动重启时，在本目录执行：fastapi dev "01-路径参数.py"
    uvicorn.run(app, host="0.0.0.0", port=8000)
