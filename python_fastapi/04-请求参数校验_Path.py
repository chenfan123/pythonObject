# 第一个fastapi程序
from fastapi import FastAPI, Query
import uvicorn
from fastapi import Path  # 路径参数

app = FastAPI()  # 创建一个FastAPI实例


@app.get("/item1/{id}")
def page_limit(id: int = Path(..., description="The ID of the item")):  # 必须传递
    return {"id": id}


@app.get("/item2/{id}")
def page_limit(id: int = Path(..., description="The ID of the item", gt=0, lt=100)):  # 必须传递,大于0,小于100
    return {"id": id}


@app.get("/item3/{id}")
# 表示正则表达式
def page_limit(id: int = Path(..., description="The ID of the item", regex="^[0-9]+$")):
    return {"id": id}


if __name__ == "__main__":
    # 传入 app 对象时不能开 reload，否则 uvicorn 会直接退出。
    # 需要改代码自动重启时，在本目录执行：fastapi dev "01-路径参数.py"
    uvicorn.run(app, host="0.0.0.0", port=8000)
