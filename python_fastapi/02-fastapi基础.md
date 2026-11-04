##### 启动服务

1. 通过命令：`uvicorn file_name:app_name --reload`
2. 通过代码：`uvicorn.run(app, host="0.0.0.0", port=8000)`
3. 通过调试：`fastapi dev filename`

### 传参方式

- 路径参数
- 查询参数
- 请求体
- 表单数据

### 参数校验

1. 原生类型注解
2. 查询参数使用 Query 类
3. 路径参数使用 Path 类
4. Field 方式
5. 表单数据使用 Form 类

## 异步与非异步

### 异步

##### 事件循环

异步代码运行在 python 的异步事件循环（如 asyncio）中，事件循环负责协调多个协程,在某个协程等待 I/O 操作时，事件循环可以切换到其他协程执行，

##### 非阻塞

当一个异步函数调用 await，他回暂停执行将控制权交回事件循环，允许其他任务运行，直到等待的操作完成。

##### 并发性

异步模式允许单个线程处理大量并发请求，特别适合高并发场景

### 非异步

##### 阻塞式执行

同步函数在调用时会完全占用线程，直到函数执行完成才会释放线程

##### 线程池

同步函数由工作线程处理，Uvicorn 会将同步函数放入线程池运行

##### 并发限制

线程池的大小限制了同步函数的并发能力，如果线程池耗尽，新的请求会排队等待，可能导致响应延迟

## 文件上传

### 基础文件上传

#### bytes 类型（适合小文件）

- 文件以二进制形式读取，适合小于 10MB 的文件
- 内存占用高，大文件可能导致崩溃

#### uploadFile 类型（推荐）

- 自动处理内存和磁盘存储（超过阈值存磁盘）
- 支持文件元数据（filename、content-type）
- 提供异步文件操作方法（read()、write())

## 请求对象 Request

- 获取客户端信息
- 获取请求头
- 获取请求体
- 获取请求查询参数
- 获取请求表单数据
- 获取请求 cookies
- 获取请求状态码
- 获取请求协议
- 获取请求主机
- 获取请求路径
- 获取请求全路径
- 获取请求引用 URL
- 获取请求 User-Agent

  ## 响应对象 Response

- JSON 响应：用于 RESTful API 的数据交互，占主导地位
- 列表响应：用于分页查询或批量数据返回
- 文件响应：用于文件下载或上传
- 字符串响应：用于健康检查或简单状态反馈
- HTML 响应：用于渲染网页内容
- 重定向响应：用于认证流程或 URL 前一
- 流式响应：用于实时数据传输或大文件处理

### JSON 响应

1. 通过`response_model`实现相应数据结构校验
2. 使用`response_model_exclude_unset=True`过滤未设置的默认值字段
3. 组合模型：`response_model=Union[SuccessResponse[User], ErrorResponse[User]]`

### 文件格式

#### 关键特点

内容类型：通过 Content-Type 头信息指定文件 MIME 类型，如 application/pdf、text/csv、application/vnd.ms-excel
文件内容：body 包含文件的实际数据，可能是二进制或文本

#### 大文件的处理

先读取文件拆分成 chunks，然后通过 StreamingResponse 返回

### 其他响应的格式

#### 字符串响应

直接返回字符串，格式为 text/plain

#### html 响应

直接返回 html 字符串，格式为 text/html

#### 重定向响应

通过 RedirectResponse 返回重定向响应，格式为 302 Found
