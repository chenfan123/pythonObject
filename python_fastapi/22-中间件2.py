# 中间件的使用
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

# 自定义中间件,实现类似于app.middleware("http")


class LogMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, request, call_next):
        print("LogMiddleware")
        return self.app(request, call_next)


@app.middleware("http")
async def middleware1(request, call_next):
    print("middleware1")
    # print(request.url, request.method)
    response = await call_next(request)
    print("middleware1 end")
    return response


@app.middleware("http")
async def middleware2(request, call_next):
    print("middleware2")
    response = await call_next(request)
    print("middleware2 end")
    return response


@app.get('/middleware')
async def get_middle():
    print("get_middle")
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
