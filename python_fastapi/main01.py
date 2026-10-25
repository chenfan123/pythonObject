# 第一个fastapi程序
from fastapi import FastAPI
import uvicorn

app = FastAPI()  # 创建一个FastAPI实例


@app.get("/")  # 定义一个路由，使用get请求
def read_root():
    return {"message": "Hello, World!"}


# 运行程序
# 1. 通过命令：uvicorn file_name:app_name --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# 2. 通过代码：`uvicorn.run(app, host="0.0.0.0", port=8000)`
# 3. 通过调试：`fastapi dev filename`
