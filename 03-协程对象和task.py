# 创建协程对象：coroutine_a = worker("A")

# 创建 Task：task_b = asyncio.create_task(worker("B"))
#
# 上一步做了2件事： 1. 创建 worker("B") 协程对象；2. 包装为 Task，并安排到事件循环中运行。遇到可以暂停的 await，事件循环才获得控制权并运行其他任务。

# 调用 async def 只会创建协程对象，不会自动执行。asyncio.create_task() 会把协程包装成 Task，并安排到事件循环中运行。Task 不会立刻抢占当前协程，而是在当前协程遇到可暂停的 await、将控制权交回事件循环后获得执行机会。
"""
coroutine = worker()       # 只创建，未调度
task = create_task(worker()) # 创建并安排运行
await coroutine            # 当前协程直接等待它
await task                 # 等待已安排的任务完成
"""
# await 是“当前协程在这里等它”
# create_task() 是“先把它登记成一个可并发调度的任务”
