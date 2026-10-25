##### 启动服务

1. 通过命令：`uvicorn file_name:app_name --reload`
2. 通过代码：`uvicorn.run(app, host="0.0.0.0", port=8000)`
3. 通过调试：`fastapi dev filename`

### 传参方式

- 路径参数
- 查询参数
- 请求体

### 参数校验

1. 原生类型注解
2. 查询参数使用 Query 类
3.
