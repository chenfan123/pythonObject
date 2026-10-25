# 逐个创建、逐个等待 → 串行
# 先安排多个任务、再等待 → 并发
import asyncio


async def fetch(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")
    return f"{name} result"


async def main():
    result_a = await fetch("A", 2)
    result_b = await fetch("B", 1)

    print(result_a)
    print(result_b)


asyncio.run(main())

# 上述就是串行等待


async def main2():
    results = await asyncio.gather(
        fetch("A", 2),
        fetch("B", 1),
    )

    print(results)
# gather() 会把多个协程安排为并发任务。
# 输出：A start -> B start -> B end -> A end -> ['A result', 'B result']
# 任务按各自速度完成，但 gather() 按传入顺序组织结果。

# 先创建Task，再依次 await
# 下面这个仍然是并发的，两个 Task 已经提前安排


async def main3():
    task_a = asyncio.create_task(fetch("A", 2))
    task_b = asyncio.create_task(fetch("B", 1))

    result_a = await task_a
    result_b = await task_b

# Task 完成后会保存：协程返回值；异常；完成或取消状态。

# gather()
# await asyncio.gather(task_a, task_b)
# 只要其中一个异常，就会把异常向外传播，无法正常返回完整结果列表。
# 默认的 gather() 传播一个异常时，不代表它一定自动取消其他任务。其他任务可能仍在运行，具体生命周期还取决于外层事件循环是否继续运行。
# return_exceptions=True：希望等待所有任务完成，并把异常放进结果列表
