# Python + FastAPI + 后端面试题池

学习追踪：[`Python_FastAPI_后端面试学习追踪_更新版.md`](./Python_FastAPI_后端面试学习追踪_更新版.md)

## 使用方式

- 本文件只维护面试题，不记录学习进度和得分。
- 题目不要求集中作答，将在后续大章节中随机穿插回测。
- 抽题会混合当前章节与历史章节，并根据回答更新学习追踪文件。
- 后续每完成一个大章节，就向对应题库补充常规问题和场景追问。

## 第1章：Python 核心基础

1. Python 中变量、对象和对象引用是什么关系？
2. `==` 和 `is` 有什么区别？为什么判断 `None` 推荐使用 `is None`？
3. 为什么不能把可变对象直接作为函数默认参数？
4. 浅拷贝和深拷贝有什么区别？嵌套列表为什么可能仍然共享？
5. Python 的参数传递为什么更适合描述为对象共享传递？
6. `*args`、`**kwargs`、`/` 和 `*` 在函数签名中分别有什么作用？
7. 什么是 LEGB？什么情况下会出现 `UnboundLocalError`？
8. 闭包是什么？什么时候需要 `nonlocal`？

## 第2章：Python 进阶

1. 装饰器在装饰阶段和调用阶段分别发生什么？
2. 为什么编写装饰器时通常要使用 `functools.wraps`？它对 FastAPI 有什么意义？
3. 多个装饰器的应用顺序、调用顺序和返回顺序分别是什么？
4. 可迭代对象、迭代器和生成器有什么区别？
5. `yield` 为什么能够实现惰性计算和流式处理？
6. 上下文管理器如何保证发生异常时仍然释放资源？
7. `__exit__` 返回 `True` 与返回假值分别意味着什么？

## 第3章：Python 异步

1. `async def` 为什么不会自动把同步阻塞代码变成异步代码？
2. 协程对象、Task 和事件循环分别是什么？
3. 连续 `await` 与先创建多个 Task 再等待有什么区别？
4. `asyncio.gather()` 如何处理结果顺序与异常？
5. 为什么 `time.sleep()` 会阻塞事件循环？如何处理同步阻塞 I/O？
6. I/O 密集和 CPU 密集任务应如何在协程、线程和进程之间选择？
7. `Lock` 与 `Semaphore` 分别解决什么问题？
8. `asyncio.Queue.join()`、`task_done()` 和消费者退出信号如何配合？
9. 超时和取消发生时为什么仍然需要 `finally`？

## 第4章：FastAPI 基础

1. FastAPI、Uvicorn 和 ASGI 分别承担什么职责？
2. Path、Query、Header、Cookie 和 Body 参数如何区分？
3. 如何选择 200、201、204、400、401、403、404、409、422、429 和 504？
4. 为什么业务错误码不能完全替代 HTTP 状态码？
5. `HTTPException` 与直接返回错误字典有什么区别？
6. `response_model` 为什么不仅是文档功能，也是安全边界？
7. PUT 与 PATCH 有什么区别？部分更新如何避免用 `None` 覆盖旧值？
8. 为什么生产环境不能用进程内字典代替数据库？

## 第5章：Pydantic

1. Pydantic 在类型注解的基础上额外提供了什么能力？
2. 必填、可空、默认值和 `default_factory` 有什么区别？
3. `field_validator` 与 `model_validator` 分别适合什么规则？
4. `model_validate()`、`model_dump()` 和 `model_dump_json()` 分别负责什么？
5. `exclude_none`、`exclude_unset` 和 `exclude_defaults` 有什么区别？
6. alias、`alias_generator` 和 `populate_by_name` 分别控制什么？
7. 为什么请求 DTO、响应 DTO、领域模型和 ORM 模型不应该默认合并？
8. 为什么数据库唯一性检查应由 Service 编排、Repository 查询，而不是放入 Pydantic 验证器？
9. 单独使用 Pydantic 时的 `ValidationError` 与 FastAPI 请求校验返回的 422 有什么关系？

## 第6章：FastAPI 原理

1. FastAPI、Uvicorn 和 ASGI 分别承担什么职责？一次 HTTP 请求如何到达路由函数？
2. WSGI 与 ASGI 的核心区别是什么？为什么 WebSocket 更适合 ASGI？
3. 一次 FastAPI 请求通常经过哪些生命周期阶段？请求校验失败时路由函数会不会执行？
4. `Depends` 如何根据函数签名构建依赖树？依赖失败后会发生什么？
5. 同一个依赖在一次请求内被多次引用时默认执行几次？`use_cache=False` 有什么作用？
6. `yield` Dependency 如何管理数据库 Session？多层资源为什么按创建顺序的反方向清理？
7. Middleware、Dependency 和 Exception Handler 的职责分别是什么？
8. 多个 Middleware 的请求顺序和响应顺序是什么？为什么称为洋葱模型？
9. Lifespan 与 `yield` Dependency 的作用范围有什么区别？Engine 与 Session 分别应放在哪里？
10. 多 Worker 部署时，Lifespan、`app.state` 和普通全局变量如何表现？
11. FastAPI 如何执行 `async def` 路由、普通 `def` 路由以及普通 `def` Dependency？
12. 为什么在异步路由中直接调用同步辅助函数仍会阻塞事件循环？
13. `await asyncio.to_thread(func, *args)` 的作用是什么？为什么不能写成 `to_thread(func())`？
14. 线程池适合什么任务？CPU 密集任务为什么通常考虑进程池、任务队列或独立服务？
15. 大量长时间同步 I/O 请求可能如何耗尽线程池？可以从哪些方向治理？
