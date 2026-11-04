from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get('/client-info')
async def client_info(request: Request):
    return {
        "请求IP": request.client.host,
        "请求端口": request.client.port,
        "请求URL": request.url,
        "请求方法": request.method,
        "请求头": request.headers,
        # "请求体": await request.body(),
        # "请求查询参数": request.query_params,
        # "请求表单数据": await request.form(),
        # "请求cookies": request.cookies,
        "请求状态码": request.status_code,
        "请求协议": request.scheme,
        "请求主机": request.host,
        "请求路径": request.path,
        "请求全路径": request.url.path,
        "请求引用URL": request.headers.get('referer'),
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
