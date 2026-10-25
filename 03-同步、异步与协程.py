import asyncio

# async def 返回协程对象():


async def get_number():
    print("执行 get_number")
    return 10

coroutine = get_number()
get_number()
# 上述代码执行流程
# 创建并返回一个协程对象,不会实际去执行函数代码
# 协程需要被 await，或交给事件循环运行。

# await 只能直接写在 async def 内部。


async def main():
    result = await get_number()  # 执行 get_number 函数，并返回 10
    print(result)
# 执行 get_number() 对应的协程；
# 当前协程等待它完成；
# 如果遇到可暂停的异步操作，执行权可交回事件循环；
# 完成后获得返回值。
asyncio.run(main())
# asyncio 创建事件循环；运行 main() 协程；管理协程暂停和恢复；完成后关闭事件循环。

# 要并发运行多个协程
"""
await asyncio.gather(
    worker("C"),
    worker("D"),
)
"""
# 交替运行：因为 asyncio 使用协作式调度
# 当前协程必须执行到一个能够暂停的 await，事件循环才能切换到其他任务。

# 协程对象与 Task
# 协程对象不会自动安排他运行
# 创建 Task，会把协程包装成 Task，并安排它尽快由事件循环运行。
# task = asyncio.create_task(worker("B"))
