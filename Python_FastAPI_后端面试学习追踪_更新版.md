# Python + FastAPI + 后端面试学习追踪（更新版）

课程目录：[`00-学习目录.md`](./00-学习目录.md)

面试题池：[`Python_FastAPI_后端面试题池.md`](./Python_FastAPI_后端面试题池.md)

## 进度与评分说明

- 学习阶段只记录为“已学 / 学习中 / 未开始”，不再用打勾表示掌握。
- 章节得分是动态诊断分，不是结课成绩；会随着练习、复习和面试表达表现更新。
- 评分参考：概念理解 30%、代码推演 25%、术语表达 20%、迁移应用 25%。
- 重点等级面向“Agent 全栈 / AI 后端开发与面试”：五星为必须重点掌握，四星为高频能力，三星为必要基础。
- 当前学习位置：第 10 章第 4 趴——依赖倒置与可测试性。
- 总体课程推进：约 36%。

## 章节重要度与学习得分

| 章节 | 主题 | 重点等级 | 当前阶段 | 学习得分 | 当前评价 |
|---|---|---:|---|---:|---|
| 1 | Python 核心基础 | ★★★★☆ | 已学，持续复习 | 8.8/10 | 对象引用和参数传递较稳，浅拷贝术语仍需精确 |
| 2 | Python 进阶 | ★★★★☆ | 已学，持续复习 | 8.5/10 | 装饰器理解较好，生成器执行顺序曾出现偏差 |
| 3 | Python 异步 | ★★★★★ | 已学，持续复习 | 8.4/10 | 并发模型已建立，事件循环、Queue 和取消语义需复习 |
| 4 | FastAPI 基础 | ★★★★★ | 已学，持续复习 | 8.9/10 | 路由、DTO、异常响应较稳，可继续强化工程边界 |
| 5 | Pydantic | ★★★★☆ | 已学，持续回测 | 8.7/10 | DTO 边界理解较好；Service 与 Repository 的职责需更精确 |
| 6 | FastAPI 原理 | ★★★★★ | 已学，持续回测 | 8.8/10 | 生命周期和调度模型较稳；`asyncio.to_thread()` 完整写法需巩固 |
| 7 | PostgreSQL | ★★★★★ | 已学，持续回测 | 8.3/10（暂定） | 事务、隔离、MVCC 与并发控制链路较稳；SQL 落笔、NULL 语义及数据库监控视图仍需复习 |
| 8 | SQLAlchemy | ★★★★★ | 学习中，暂缓 | — | 已学 ORM 映射基础；Engine、Session、事务和异步 ORM 待继续 |
| 9 | Redis | ★★★★★ | 已学，持续回测 | 8.8/10 | 数据结构、TTL、缓存治理、锁、限流、Session 与任务状态链路已建立；需持续回测持久化边界、锁租期与生产 Worker 可靠性 |
| 10 | 后端架构 | ★★★★★ | 学习中（第 3 趴完成） | 8.6/10（暂定） | 已能串起 Router、依赖装配、Service、事务、领域异常与接口测试；DTO、ORM 与领域模型的职责已建立，依赖倒置与更细粒度测试待继续强化 |
| 11 | 并发 | ★★★★★ | 未开始 | — | I/O/CPU 任务选型、线程/进程/协程安全是重点 |
| 12 | 高并发 | ★★★★★ | 未开始 | — | 限流、超时、重试、熔断和背压是重点 |
| 13 | 消息队列 | ★★★★☆ | 未开始 | — | 可靠投递、幂等、削峰和最终一致性是重点 |
| 14 | 网络 | ★★★★★ | 未开始 | — | HTTP/TCP、WebSocket、SSE、超时重连是重点 |
| 15 | 安全 | ★★★★★ | 未开始 | — | JWT、OAuth2、CORS/CSRF 和注入防护是重点 |
| 16 | Docker 与部署 | ★★★★☆ | 未开始 | — | 容器网络、健康检查、Worker 和 Nginx 是重点 |
| 17 | Agent Backend | ★★★★★ | 未开始 | — | RAG、流式输出、工具调用、状态和长任务是核心 |
| 18 | 系统设计 | ★★★★★ | 未开始 | — | 高并发 Agent/RAG、可靠性和成本治理是核心 |
| 19 | 综合项目 | ★★★★★ | 未开始 | — | 用 FastAPI、PG、Redis 和 Agent 串联全部能力 |
| 20 | 模拟面试 | ★★★★★ | 未开始 | — | 检验解释、追问、编码和系统设计能力 |

## 当前综合能力评分

| 维度 | 得分 | 主要观察 |
|---|---:|---|
| 概念理解 | 8.9/10 | 大部分核心概念能解释原因 |
| 代码推演 | 8.5/10 | 常规题稳定，生成器和异步调度需更严格逐行推演 |
| 术语表达 | 8.1/10 | 偶尔混用“地址、指针、变量修改”等不精确说法 |
| 迁移应用 | 8.6/10 | 能联系 Node.js/后端场景，边界设计正在形成 |
| 当前综合分 | 8.6/10 | 已具备良好基础，下一阶段重心是原理和工程化 |

## 后续教学与考核规则

- 每一趴按照“概念讲解 → 场景示例 → 重点总结 → 多类型练习”推进。
- 每趴结尾必须给出重点总结，明确“必须掌握、容易混淆、面试表达”三类内容。
- 练习不再以“预测代码输出”为主；会混合概念解释、代码阅读、错误诊断、方案选择、代码补全、业务场景和面试追问。
- 面试题不集中在某一趴一次考完，而是在后续大章节中随机穿插，回测当前章节与历史章节。
- 每个大章节都包含本章面试题和跨章节旧知识回测；回答结果用于动态调整章节得分和薄弱点。
- 随机回测应提供足够上下文；答错后按“题目上下文 → 问题 → 目前回答 → 标准回答 → 状态”写入错题本。
- 从 PostgreSQL 第 4 趴开始采用“先建立画面，再补术语”的讲法：是否拆分、拆成几回合，按知识难度和当轮掌握情况动态决定，不设固定回合数；每回合只引入一个核心关系。
- 数据库练习采用阶梯式输出：先做选择/判断和改错，再做半成品补空，确认理解后才要求独立写完整 SQL；不再每题都从零手写 SQL。
- 每个新概念优先使用生活类比、数据流图或小表格说明，并在结尾提供一句记忆口令和一个真实后端场景。
- 如果 SQL 写错，先判断是概念错误还是仅语法/字段名错误，分别评分，避免语法细节掩盖真实理解。
- 每一趴和每个小回合开始前，先明确说明“学习目标”和“本节重点”，让学习者知道这一段要解决什么问题、结束时应能做到什么。
- 每个小节必须完整走完“学习目标与重点 → 具体业务场景 → 原理分步讲解 → 最小代码/命令或执行推演 → 学生作答 → 逐题解析与小结”再进入下一节；不得只列目标/重点便立刻提问后跳转。
- 上述教学链路按知识类型弹性使用，不机械要求每段都出现业务案例、实验和固定题数：纯概念可直接讲解并配关键辨析；时序/并发适合推演；代码与外部状态才做实验；仅在需要验证理解或进行历史回测时提问。无论形式如何，进入下一节前仍需完成必要解释与本节收束。
- 每个可运行示例按主题使用独立文件或独立目录；不得把缓存、限流、任务状态等不相关实验持续堆叠到同一个入口文件。
- 用户提交练习答案后，先逐题解析：结论是否正确、正确原因、错误/不精确处及改进表达；不得只给总分或泛化评价。
- 每个小回合在批改后给出“本轮小结”，回扣开头的学习目标与重点，明确“已掌握、仍需注意、真实场景怎么用”。
- 每一趴或一章完成时，再给出“章节复盘”：目标达成情况、核心链路、易错点、面试表达与下一步衔接；不在尚未完成下一趴前提前输出泛化回扣。
- 小结与复盘只能归纳已实际讲解和练习过的知识；尚未讲解的方案必须单列为“后续预告”，不能与已掌握内容混写，也不能据此考核学习者。
- Redis 章节采用“先实操、后抽象”模式：每趴优先完成一个可观察的小实验（Redis CLI 或 FastAPI 接口），再用少量场景题提炼原理；只有涉及并发、过期、锁和故障策略时才增加必要的推演题。
- Redis 实操不豁免历史回测：每个实验完成后的批改与小结必须追加 1～2 道跨章节回顾题，来源按 Python、异步、FastAPI、Pydantic、PostgreSQL 轮换；题目提供完整必要上下文，避免只考孤立术语。
- 练习形式保持混合：简答、判断、排序、错误诊断、方案选择、半成品补空、生活场景与少量 SQL；选择题只用于快速确认概念，不作为唯一形式。
- 每个小回合结束至少加入一道“历史知识随机回测”，题目来源从第 1 章开始跨章节轮换，并明确标注来源章节；不只回测最近学习的内容。

题目本体统一维护在独立的[面试题池](./Python_FastAPI_后端面试题池.md)中，本文件只记录抽题结果、分数变化、薄弱点和错题。

## 动态薄弱点（持续更新）

### 🟥 1. 官方术语表达

目前： - 修改变量 - 地址 - 地址指针

建议： - 变量重新绑定（Rebinding） - 对象引用（Reference） -
对象（Object）

### 🟥 2. 回答深度

回答时增加： 是什么 → 为什么 → 底层原因

### 🟥 3. 代码执行顺序与读取时机

先完成所有赋值和函数调用，再执行 print 时，需要根据 print 当下的对象状态判断输出。

### 🟥 4. 浅拷贝的准确描述

浅拷贝只创建新的外层容器；不会自动重新创建容器中的不可变对象或嵌套可变对象，而是复制其中的对象引用。

## 错题本（持续更新）

### 错题1

题目上下文：

```python
a = 10
b = a
b = 20

print(a)
print(b)
```

问题：为什么 b=20 没影响 a？

目前回答： 创建了新的 int 对象。

标准回答： int 属于不可变对象，因此不会修改原对象，而是让变量 b
重新绑定到新的对象。

状态：🟨

### 错题2

题目上下文：

```python
a = {"name": "Alice"}
b = a
b["name"] = "Bob"

print(a)
print(b)
```

问题：为什么 dict 修改后 a 也变了？

目前回答： 地址指针。

建议： a 与 b 引用同一个 dict 对象，因此修改的是共享对象。

状态：🟨

### 错题3

题目上下文：

```python
def create_user(name, tags=[]):
    tags.append("new")
    return {"name": name, "tags": tags}


user1 = create_user("Alice")
user2 = create_user("Bob")

print(user1)
print(user2)
```

问题：两个函数调用共享可变默认列表，先完成两次调用再打印 user1，user1 的 tags 是什么？

目前回答：`['new']`

标准回答：`['new', 'new']`。user1 和 user2 的 tags 引用同一个列表；第二次调用修改共享列表后，再打印 user1 时也会观察到修改后的状态。

状态：🟨

### 错题4

题目上下文：

```python
def create_user(name, tags=None):
    if tags is None:
        tags = []
    tags.append("new")
    return {"name": name, "tags": tags}


shared_tags = ["vip"]
user1 = create_user("Alice", shared_tags)
user2 = create_user("Bob", shared_tags)

print(user1["tags"])
print(user2["tags"])
```

问题：`print(user1["tags"])` 和 `print(user2["tags"])` 输出什么？

目前回答：输出整个用户字典，且第二个用户名误写为 Alice。

标准回答：两个表达式只读取 `tags` 字段，因此都输出 `['vip', 'new', 'new']`；要严格区分打印整个对象与打印对象中的字段。

状态：🟨

### 错题5

题目上下文：

```python
original = {
    "name": "Alice",
    "skills": ["Python", "FastAPI"],
}

copied = original.copy()
copied["name"] = "Bob"
copied["skills"].append("Redis")
```

问题：为什么浅拷贝后给 `copied["name"]` 赋值不影响原字典？

目前回答：浅拷贝重新创建了第一层的不可变数据。

标准回答：浅拷贝只创建新的外层字典，初始值的引用被复制；给 `copied["name"]` 赋值是在修改新字典自己的键值绑定。它不会修改字符串对象，也不会修改原字典的键值绑定。

状态：🟨

### 错题6

题目上下文：

```python
def show(name, age=18, *skills, **profile):
    print(skills)
    print(profile)


show(
    "Alice",
    20,
    "Python",
    "FastAPI",
    city="Shanghai",
    level="junior",
)
```

问题：函数定义中的 `*skills` 收集多个位置参数后是什么类型？

目前回答：数组类型。

标准回答：Python 没有 JavaScript 意义上的 Array；`*skills` 在函数定义中将多余位置参数收集为 `tuple`。`**profile` 将多余关键字参数收集为 `dict`。

状态：🟨

### 错题7

题目上下文：

```python
def calculate(operation, *numbers, **options):
    print(operation)
    print(numbers)
    print(options)


calculate("sum", 10, 20, 30, precision=2, log=True)
```

问题：`def calculate(operation, *numbers, **options)` 中，多余的位置参数由谁接收？没有多余位置参数时 `numbers` 是什么？

目前回答：用 `**` 接收多余的关键词参数来解释位置参数；无额外位置参数时猜测为 `None`。

标准回答：`operation` 先接收第一个位置参数，`*numbers` 将剩余位置参数收集成元组；`**options` 只收集额外关键字参数。没有额外位置参数时，`numbers` 是空元组 `()`。

状态：🟨

### 错题8

题目上下文：

```python
x = 10


def change():
    print(x)
    x = 20


change()
```

问题：函数先读取 `x`、后给 `x` 赋值时，会产生什么异常？

目前回答：参数未定义相关错误。

标准回答：`UnboundLocalError`。只要函数体内对名称 `x` 有赋值，Python 就会把它判定为该函数的局部名称（除非声明 `global` 或 `nonlocal`）；执行到赋值前读取它时，局部名称尚未绑定。

状态：🟨

### 错题9

题目上下文：

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
print(double(10))
```

问题：`make_multiplier(2)` 与 `double(10)` 中，哪一步返回内部函数，闭包如何保留 `factor`？

目前回答：`double(10)` 返回了新函数，`factor` 被透传。

标准回答：`make_multiplier(2)` 返回内部函数对象并赋给 `double`；该函数形成闭包，捕获外层作用域中 `factor` 的绑定。`double(10)` 是调用这个已保存的函数并返回计算结果。

状态：🟨

### 错题10

题目上下文：

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


print(add(2, 3))
```

问题：`@log_call` 如何展开，装饰后的 `add(2, 3)` 首先执行哪个函数？

目前回答：展开为 `log_call(add(2, 3))`，调用时先执行原始 `add`。

标准回答：展开为 `add = log_call(add)`，传入的是原始函数对象而不是调用结果。重新绑定后，`add` 指向 `wrapper`，所以 `add(2, 3)` 首先执行 `wrapper`，再由闭包中的 `func` 调用原始 `add`。

状态：🟨

### 错题11

题目上下文：

```python
from functools import wraps


def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("检查权限")
        return func(*args, **kwargs)

    return wrapper


@authorize
def delete_user(user_id: int):
    """删除指定用户。"""
    return f"deleted: {user_id}"


print(delete_user.__name__)
print(delete_user.__doc__)
print(delete_user(10))
```

问题：使用 `@wraps(func)` 后，读取 `__name__`、`__doc__` 是否会执行包装函数？调用装饰后的函数时是否再次执行外层装饰器？

目前回答：每次读取元数据都会打印包装逻辑；调用时先执行外层 `authorize`。

标准回答：读取属性不会调用函数；`@wraps` 只更新包装函数的元数据。`authorize` 在函数定义完成后的装饰阶段执行一次并返回 `wrapper`；运行时调用装饰后的名称，首先执行的是 `wrapper`，再由闭包中的 `func` 调用原函数。

状态：🟨

### 错题12

题目上下文：

```python
from functools import wraps


def trace(func):
    print("1：执行 trace")

    @wraps(func)
    def wrapper():
        print("2：执行 wrapper")
        return func()

    return wrapper


@trace
def job():
    print("3：执行原始 job")
    return "4：job 的结果"
```

问题：装饰器执行时定义了内部 `wrapper`，是否等于执行了 `wrapper` 的函数体？

目前回答：`trace` 和 `wrapper` 都在装饰阶段执行。

标准回答：装饰阶段会执行 `trace(func)`，创建并返回 `wrapper` 函数对象，但不会执行 `wrapper` 的函数体。只有调用装饰后的 `job()` 时才执行 `wrapper` 中的语句。

状态：🟨

### 错题13

题目上下文：

```python
from functools import wraps


def repeat(times):
    print(f"A: repeat({times})")

    def decorator(func):
        print(f"B: decorator({func.__name__})")

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("C: wrapper")
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=2)
def greet(name):
    print(f"Hello, {name}")
    return name.upper()


print("D: 准备调用")
print(greet("Alice"))
```

问题：带参数装饰器的 `wrapper` 循环调用原函数两次，外层再执行 `print(greet(...))` 时，完整输出是什么？

目前回答：只写出一次原函数输出，并遗漏外层 `print` 打印的返回值。

标准回答：装饰阶段先输出 A、B；调用前输出 D；调用阶段输出 C，循环使 `Hello, Alice` 出现两次；最后外层 `print` 输出包装函数返回的 `ALICE`。

状态：🟨

### 错题14

题目上下文：

```python
def decorator_a(func):
    def wrapper(*args, **kwargs):
        print("A before")
        result = func(*args, **kwargs)
        print("A after")
        return result
    return wrapper


def decorator_b(func):
    def wrapper(*args, **kwargs):
        print("B before")
        result = func(*args, **kwargs)
        print("B after")
        return result
    return wrapper


@decorator_a
@decorator_b
def work():
    print("work")
    return 100


print(work())
```

问题：多装饰器包装的原函数返回 `100`，且每层都正确 `return result` 时，最外层输出什么？

目前回答：`10`。

标准回答：`100`。每一层 wrapper 都将内层返回值原样向外传递，最终由最外层 `print` 输出原函数返回的 `100`。

状态：🟨

### 错题15

题目上下文：

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


counter = Countdown(3)
print(next(counter))
print(list(counter))
print(list(counter))
```

问题：对同一个迭代器连续两次执行 `list(iterator)`，第二次为什么是空列表？

目前回答：第二次仍得到第一次的剩余元素。

标准回答：`list(iterator)` 会持续调用 `next()`，直到捕获 `StopIteration`，因此第一次转换已消耗所有剩余元素。同一个迭代器耗尽后不会自动重置，第二次转换得到 `[]`。

状态：🟨

### 错题16

题目上下文：

```python
def countdown(start):
    print("start")
    while start > 0:
        print(f"before yield: {start}")
        yield start
        print(f"after yield: {start}")
        start -= 1
    print("end")


generator = countdown(2)
print("A")
print(next(generator))
print("B")
print(next(generator))
```

问题：生成器函数何时执行函数体，`yield` 在哪里暂停，`print(next(generator))` 会产生哪些输出？

目前回答：创建生成器时立即输出 `start`；第一次 `next()` 在下一轮 `yield 1` 处暂停；遗漏 `next()` 产出的 `2`、`1` 以及调用前的 `A`。

标准回答：调用含 `yield` 的生成器函数只创建生成器对象，不执行函数体；第一次 `next()` 才从函数开头运行，并在当前轮 `yield 2` 处产出 `2` 后暂停。外层 `print(next(...))` 还会打印产出的值。下一次 `next()` 从该 `yield` 之后恢复。

状态：🟩 已通过针对性复习

### 错题17

题目上下文：

```python
class Resource:
    def __enter__(self):
        print("open")
        return "resource object"

    def __exit__(self, exc_type, exc_value, traceback):
        print("close")
        if exc_type is not None:
            print(exc_type.__name__)
        return True


with Resource() as value:
    print(value)
    raise ValueError("boom")
```

问题：`__exit__` 中打印 `exc_type.__name__` 时输出异常类型还是异常消息？

目前回答：输出 `boom`。

标准回答：输出 `ValueError`，因为 `exc_type` 是异常类；`exc_type.__name__` 是类名。异常消息 `boom` 保存在 `exc_value` 中，打印 `exc_value` 才会得到它。

状态：🟨

### 错题18

题目上下文：

```python
from contextlib import contextmanager


@contextmanager
def resource():
    print("A")
    try:
        yield "B"
    finally:
        print("C")


try:
    with resource() as value:
        print(value)
        raise RuntimeError("E")
except RuntimeError as error:
    print(error)

print("F")
```

问题：`@contextmanager` 中只有 `try/finally`，外层 `try/except` 捕获异常后程序继续，是否说明上下文管理器吞掉了异常？

目前回答：吞掉了异常，上下文管理器默认返回 `True`。

标准回答：没有吞掉。异常会在 `yield` 处重新进入生成器，先执行 `finally`，随后继续向外传播；外层 `except` 捕获它并打印异常消息，因此程序才能继续。生成器上下文管理器不存在“默认返回 True”的规则；只有在生成器内部捕获异常且不重新抛出时才会抑制它。

状态：🟨

### 错题19

题目上下文：

```python
from contextlib import contextmanager


@contextmanager
def resource():
    try:
        yield "B"
    except RuntimeError as error:
        print(f"handled: {error}")
        raise
    finally:
        print("C")


with resource() as value:
    print(value)
    raise RuntimeError("E")

print("F")
```

问题：生成器上下文管理器的 `except` 中重新 `raise`，即使后面还有 `finally`，异常是否仍会传播，with 后代码是否执行？

目前回答：仍会执行 with 后代码，因为还有 `finally`。

标准回答：`finally` 保证清理逻辑执行，但不抑制异常。`except` 中的 `raise` 会重新抛出当前异常；随后先执行 `finally`，再继续向外传播。如果外层没有捕获，with 后代码不会执行。

状态：🟨

### 错题20

题目上下文：

```python
from contextlib import contextmanager


@contextmanager
def resource():
    print("open")
    try:
        yield
    finally:
        print("close")


try:
    with resource():
        print("work")
        raise ValueError("failed")
except ValueError:
    print("outer handled")
```

问题：生成器上下文管理器进入 with 时，`yield` 前的资源初始化输出是否会执行？

目前回答：完整输出中遗漏 `open`。

标准回答：会先输出 `open`。进入 with 时，`@contextmanager` 会驱动生成器运行到 `yield`，因此所有 `yield` 前的初始化代码先执行。

状态：🟨

### 错题21

题目上下文：

```python
import asyncio


async def task():
    print("A")
    await asyncio.sleep(0)
    print("B")
    return 10


async def main():
    coroutine = task()
    result = await coroutine
    print(result)


asyncio.run(main())
```

问题：`await asyncio.sleep(0)` 是否表示真实延迟，`await coroutine` 如何得到结果？

目前回答：sleep 是延迟执行；await 让 result 去接收。

标准回答：`asyncio.sleep(0)` 主要用于让出执行权给事件循环，使其他就绪任务有机会运行，通常不产生有意义的等待时长。`await coroutine` 驱动并等待协程完成，并取得协程通过 `return` 返回的值。

状态：🟨

### 错题22

题目上下文：

```python
import asyncio


async def worker(name):
    print(f"{name} start")

    # 没有任何会暂停的 await
    for _ in range(10_000_000):
        pass

    print(f"{name} end")


async def main():
    await asyncio.gather(
        worker("C"),
        worker("D"),
    )


asyncio.run(main())
```

问题：`async def` 内没有任何会暂停的 `await` 时，`asyncio.gather()` 能否让多个协程交替执行？

目前回答：可以，因为 worker 是异步函数。

标准回答：不能仅凭 `async def` 自动交替。asyncio 是协作式调度，当前协程必须执行到可暂停的 `await` 才会把控制权交还事件循环；没有暂停点时，一个协程开始后会运行到结束，再运行其他协程。

状态：🟨

### 错题23

题目上下文：

```python
task_a = asyncio.create_task(job("A", 2))
task_b = asyncio.create_task(job("B", 1))

result_a = await task_a
result_b = await task_b

print([result_a, result_b])
```

其中 `job()` 最终执行 `return name`。

问题：`[result_a, result_b]` 保存的是 Task 状态，还是协程返回值？

目前回答：保存 Task 的协程返回值、异常和状态。

标准回答：Task 对象内部会跟踪完成状态并保存结果或异常；但 `await task_a` 和 `await task_b` 会提取各自协程通过 `return` 返回的值。因此 `result_a == "A"`、`result_b == "B"`，列表是 `["A", "B"]`。

状态：🟨

### 错题24

题目上下文：

```python
async def job(name, delay, fail=False):
    print(f"{name} start")
    await asyncio.sleep(delay)
    if fail:
        print(f"{name} error")
        raise ValueError(f"{name} failed")
    print(f"{name} end")
    return f"{name} ok"


async def main():
    results = await asyncio.gather(
        job("A", 2),
        job("B", 1, fail=True),
    )
    print(results)


asyncio.run(main())
```

问题：删除 `return_exceptions=True` 后，B 失败时 gather、A 和事件循环分别会怎样？

目前回答：发生异常直接抛出。

标准回答：默认 gather 会把 B 的 `ValueError` 传播给等待它的 `main()`，且不会返回结果列表；gather 本身不会因这个异常自动取消 A。但本例没有捕获异常，`main()` 退出后 `asyncio.run()` 开始关闭事件循环并取消尚未完成的 A，所以通常看不到 `A end`。要判断其他任务是否继续，必须同时考虑 gather 行为和事件循环生命周期。

状态：🟨

### 错题25

题目上下文：

```python
async def worker():
    print("start")
    try:
        await asyncio.sleep(2)
        print("end")
        return "success"
    except asyncio.CancelledError:
        print("cancelled")
        raise
    finally:
        print("cleanup")


async def main():
    try:
        result = await asyncio.wait_for(worker(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("timeout")
    print("after")
```

问题：取消由哪里发起，`CancelledError` 在哪里进入 worker，为什么捕获后通常要重新 raise？超时改为 3 秒时完整输出是什么？

目前回答：异常在外层 `await wait_for(...)` 这一行进入；重新 raise 是为了“不是直接抛出异常”；成功时只说明返回 success，未写完整输出。

标准回答：`wait_for` 到期后发起取消；`CancelledError` 在 worker 当前暂停的 `await asyncio.sleep(2)` 处被注入。捕获后通常重新 raise，以继续传播取消信号，保持任务的取消语义。timeout=3 时任务正常完成，但 finally 仍执行，输出依次为 `start`、`end`、`cleanup`、`success`、`after`。

状态：🟨

### 错题26

题目上下文：

```python
import asyncio
import time


async def blocking_job():
    print("A start")
    time.sleep(2)
    print("A end")


async def async_job():
    print("B start")
    await asyncio.sleep(1)
    print("B end")


async def main():
    start = time.perf_counter()
    await asyncio.gather(blocking_job(), async_job())
    print(round(time.perf_counter() - start))


asyncio.run(main())
```

问题：完整输出顺序是什么？B 能否在 A 的 `time.sleep(2)` 期间开始？

目前回答：`A start → B start → A end → B end → 3`，同时又说明 A 会阻塞事件循环。

标准回答：`A start → A end → B start → B end → 3`。`time.sleep(2)` 阻塞运行事件循环的线程，在它返回前事件循环无法调度 B，因此两个等待时间实际相加，耗时约 3 秒。

状态：🟨

### 错题27

题目上下文：

```text
场景 A：使用异步 PostgreSQL 驱动执行大量查询。
场景 B：调用远程 Embedding API。
场景 C：在本机执行 CPU 密集的 Embedding/文档计算。
```

问题：三个场景分别应优先选择协程、线程还是进程/Worker？

目前回答：异步 PostgreSQL 可能使用线程加协程；Embedding 涉及计算时可以考虑线程。

标准回答：场景 A 使用协程配合数据库连接池，异步驱动无需额外线程；场景 B 对当前服务是网络 I/O，异步 SDK 用协程，只有同步 SDK 才考虑线程；场景 C 的计算发生在本机，属于 CPU 密集，应优先考虑进程池、独立 Worker 或专用推理服务，而不是普通线程。

状态：🟨

### 错题28

题目上下文：

```python
queue = asyncio.Queue()

await queue.put("任务1")
await queue.put("任务2")


async def consumer(queue):
    item = await queue.get()
    try:
        print(f"处理：{item}")
    finally:
        queue.task_done()
```

问题：消费者第一次 `get()` 取得哪个任务，Queue 默认遵循什么顺序？

目前回答：取得任务1，因为它是“最新进入”的任务。

标准回答：取得任务1，但它是最早进入的任务。`asyncio.Queue` 默认遵循 FIFO（First In, First Out，先进先出），不是后进先出。

状态：🟨

### 错题29

题目上下文：

```python
await queue.put("任务1")
await queue.put("任务2")
await queue.put(None)
```

问题：这些操作应描述为“进栈”还是“入队”？默认取出顺序是什么？

目前回答：三个任务按照顺序“进栈”，再按先进先出取出。

标准回答：应描述为“入队”。Queue 是队列，默认 FIFO（先进先出）；Stack 才是栈，通常 LIFO（后进先出）。因此取出顺序为任务1、任务2、None。

状态：🟨

### 错题30

题目上下文：

```python
api = FastAPI()


@api.get("/health")
async def health():
    return {"status": "ok", "service": "learning-api"}
```

问题：请求 `POST /health` 时通常返回什么状态码？它与请求不存在路径有什么区别？

目前回答：忘记方法不匹配的状态码，并认为不重要。

标准回答：返回 `405 Method Not Allowed`，表示路径 `/health` 存在，但不支持 POST。请求未注册的路径通常返回 `404 Not Found`。二者是路由调试和 API 语义中的基础区别。

状态：🟨

### 错题31

题目上下文：

```python
@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[int, Path(gt=0)],
    keyword: Annotated[str | None, Query(min_length=2)] = None,
    page: Annotated[int, Query(ge=1)] = 1,
):
    ...
```

问题：请求 `/products/0` 和 `?keyword=a` 为什么会校验失败，状态码通常是什么？

目前回答：`product_id=0` 可以通过，因为最小值是 0；keyword 至少需要“两位数”。

标准回答：`gt=0` 表示严格大于 0，不包含 0，所以 `/products/0` 校验失败；`min_length=2` 表示字符串至少两个字符，不是数值位数。两种参数校验失败通常都返回 422。

状态：🟨

### 错题32

题目上下文：

```python
raise HTTPException(
    status_code=404,
    detail={
        "code": "USER_NOT_FOUND",
        "message": "User not found",
    },
)
```

问题：FastAPI 默认生成的 JSON 响应体是什么？HTTP 状态码与业务错误码分别表达什么？

目前回答：响应体直接是 `{"code": ..., "message": ...}`；状态码是 HTTP 请求的错误，业务错误码是包装后透露给用户或前端的内容。

标准回答：默认响应体会包裹为 `{"detail": {"code": "USER_NOT_FOUND", "message": "User not found"}}`。HTTP 状态码表达跨系统通用的协议结果类别，例如 404；业务错误码表达应用内部稳定、具体、可供客户端程序判断的原因，例如 `USER_NOT_FOUND`。

状态：🟨

### 错题33

题目上下文：

```python
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None


changes = payload.model_dump(exclude_unset=True)


@app.delete(
    "/users/{user_id}",
    status_code=204,
)
async def delete_user(user_id: int) -> Response:
    del users[user_id]
    return Response(status_code=204)


users: dict[int, UserResponse] = {}
```

问题：`exclude_unset=True`、显式空 `Response(204)` 和内存字典各自解决或暴露什么问题？

目前回答：PATCH 未传字段会默认为 None 并影响其他字段；删除成功需要“显示返回”；内存字典会造成 I/O 过高，并存在竞态和 Worker 不共享问题。

标准回答：`exclude_unset=True` 只保留客户端实际提交的字段，区分“字段未传”与“显式传 null”，避免 PATCH 意外覆盖其他字段。204 表示成功但没有响应体，显式返回空 Response 是为了确保响应体为空，而不是展示返回内容。内存字典访问速度快、几乎没有外部 I/O；真正问题是重启丢数据、多进程不共享、缺少事务/持久化/跨进程并发控制，以及数据增长占用进程内存。

状态：🟨

### 错题34

题目上下文：

```python
class ProductCreateDTO(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    active: bool = True


raw_data = {
    "name": "  Keyboard  ",
    "price": "99.5",
    "stock": 0,
    "active": "false",
}
```

问题：`stock=0` 能否通过？为什么 Create、Update、Response DTO 不应强行合并？

目前回答：`stock=0` 不能通过；三个 DTO 是“不同的用户，需要不同参数”。

标准回答：可以通过，因为 `ge=0` 表示大于等于 0；`gt=0` 才是严格大于 0。三个 DTO 面向不同的数据传输场景与职责：Create 定义创建输入，Update 定义可修改字段及可选性，Response 定义安全输出边界，并不是对应不同用户。

状态：🟨

### 错题35

题目上下文：

```python
class SignupDTO(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=8)
    password_confirm: str = Field(min_length=8)

    @field_validator("username")
    @classmethod
    def normalize_username(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized in {"admin", "root"}:
            raise ValueError("Reserved username")
        return normalized

    @model_validator(mode="after")
    def validate_passwords(self) -> Self:
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self
```

问题：输入用户名 `"  Alice  "` 后最终值是什么？验证器内部抛出 ValueError 后，Pydantic/FastAPI 对外表现为何？

目前回答：最终 username 是 `"Alice"`；保留用户名或密码不一致时直接得到 ValueError。

标准回答：`.strip().lower()` 后最终是 `"alice"`。验证器内部使用 `raise ValueError(...)` 报告字段/模型问题，Pydantic 会将它汇总进 `ValidationError`；如果模型位于 FastAPI 请求边界，框架通常再转换成 HTTP 422 响应。

状态：🟨

### 错题36

题目上下文：

```python
class ChatRequestDTO(BaseModel):
    messages: list[MessageDTO] = Field(min_length=1)
    tags: set[str] = Field(default_factory=set)
    metadata: dict[str, str] = Field(default_factory=dict)
```

问题：未传 `metadata` 时默认值是什么类型和值？

目前回答：`[]`。

标准回答：`metadata` 的类型是 `dict[str, str]`，`default_factory=dict` 每次创建一个新字典，因此默认值是 `{}`。`tags` 才通过 `default_factory=set` 获得空集合 `set()`。

状态：🟨

### 错题37

题目上下文：

```python
class ProfileDTO(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    user_id: int
    display_name: str
    bio: str | None = None


profile = ProfileDTO.model_validate(
    {"userId": "10", "displayName": "Alice"}
)
```

问题：`model_dump(by_alias=True)` 是否有别名可用？`populate_by_name=True` 与 alias_generator 分别负责什么？

目前回答：没有设置别名；Python 内外命名不同是因为 `populate_by_name=True`。

标准回答：`alias_generator=to_camel` 已自动为字段生成 `userId`、`displayName` 等别名，所以 `by_alias=True` 会使用这些名称。alias/alias_generator 定义外部别名；`populate_by_name=True` 只是额外允许输入时使用 Python 字段名，例如 `user_id`，并不负责生成别名。

状态：🟨

### 错题38

题目上下文：

```python
class UserCreateDTO(BaseModel):
    username: str
    password: str


class UserResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
```

问题：创建用户时需要查询数据库判断用户名是否重复，这条规则应该放在 Pydantic 验证器、Service 还是 Repository？三者如何配合？

目前回答：应该放在 Repository；Service 适合需要 I/O 的业务规则，Repository 适合访问外部资源并负责具体读写。

标准回答：Pydantic 负责不依赖 I/O 的输入结构和纯数据校验；Service 负责“用户名必须唯一”这条业务规则，并编排查询、错误转换和创建流程；Repository 只提供 `get_by_username()`、`save()` 等持久化操作。也就是 Service 调用 Repository 查询，再根据查询结果决定抛出冲突错误还是继续创建。

复测回答：Service 负责业务层面的校验；Repository 负责 I/O 层面的“校验”，例如入库和查询。

复测反馈：方向接近，但 Repository 不负责业务校验。它负责执行查询和持久化；Service 使用查询结果判断唯一性规则是否满足。

状态：🟨

### 错题39

题目上下文：

```python
@app.get("/report")
async def create_report():
    time.sleep(10)
    return {"status": "done"}
```

问题：这个接口有什么问题？ASGI 为什么不能自动解决？应该如何根据实际工作处理？

目前回答：同步睡眠会阻塞事件循环；可以改成 `asyncio.sleep(10)`，或者创建线程。

标准回答：`time.sleep()` 会占住事件循环线程，ASGI 只提供异步接口，不会把同步操作自动异步化。如果这 10 秒只是在等待且存在异步 API，应 `await` 对应的真实异步操作；只有示例中的“纯延迟”才能直接替换为 `asyncio.sleep()`。如果报表依赖同步阻塞 I/O，可使用 `asyncio.to_thread()` 或同步路由的线程池；如果是重 CPU 计算，应考虑进程池或任务队列，而不是线程。

状态：🟨

### 错题40

题目上下文：

```text
请为以下职责选择 Middleware、Service 或 Repository：
1. 为每个请求生成 Request ID
2. 判断用户余额是否足够支付订单
3. 根据用户 ID 查询数据库
4. 记录所有接口的响应耗时
5. 创建订单并扣减余额的业务流程
```

问题：第 5 项“创建订单并扣减余额的业务流程”属于哪一层？

目前回答：Repository。

标准回答：属于 Service。Service 负责业务用例和流程编排，例如检查余额、创建订单、扣减余额并协调事务；Repository 只提供读取账户、保存订单、更新余额等数据访问操作，不决定完整业务流程。

状态：🟨

### 错题41

题目上下文：

```text
请判断以下功能更适合 Middleware 还是 Dependency：
1. 为所有请求记录耗时
2. 只允许管理员访问某个接口
3. 获取当前租户信息并注入路由
4. 为所有响应添加安全响应头
5. 为部分路由提供数据库 Session
```

问题：第 5 项“为部分路由提供数据库 Session”更适合放在哪里？

目前回答：Middleware。

标准回答：更适合 Dependency。数据库 Session 是部分路由所需的资源，需要将对象注入路由或下游依赖，并在请求结束后可靠释放；`Depends` 配合 `yield` 可以清晰地表达创建、使用和清理。Middleware 更适合所有请求共有的 HTTP 横切处理，如耗时、Request ID 和响应头。

状态：🟨

### 错题42

题目上下文：

```text
请判断以下操作的职责：
1. 创建数据库 Session
2. 关闭数据库 Session
3. 判断用户余额是否足够
4. 提交订单事务
5. 发生数据库错误后回滚事务
6. 根据用户 ID 查询数据
```

问题：`rollback` 属于资源生命周期管理还是事务管理？查询用户属于什么职责？

目前回答：1、2、5 属于资源生命周期，其他都属于事务/业务管理。

标准回答：创建和关闭 Session 属于资源生命周期；`commit` 和 `rollback` 属于事务管理；判断余额属于 Service 的业务规则；根据用户 ID 查询属于 Repository 的数据访问职责。关闭 Session 与回滚事务不能混为一谈。原题把查询硬分到两个类别并不严谨，查询应单独归为数据访问。

状态：🟨

### 错题43

题目上下文：

```python
@app.get("/data")
async def get_data():
    result = sync_database_client.query()
    return result
```

问题：同步数据库客户端没有异步版本时，如何避免直接阻塞事件循环？

目前回答：可以创建线程，使用 `use_thread`。

标准回答：方向正确，应使用准确 API：`await asyncio.to_thread(sync_database_client.query)`；也可根据框架场景使用同步路由交给线程池。线程适合同步阻塞 I/O，不适合重 CPU 计算。

复测上下文：在 `async def` 路由中调用同步辅助函数，以及修正 `await asyncio.to_thread(sync_client.fetch())`。

复测回答：写成 `return async to_thread(query_legacy_database)`；修正时只回答 `sync_client.fetch`。

复测反馈：仍需完整写出 `return await asyncio.to_thread(query_legacy_database)` 或 `result = await asyncio.to_thread(sync_client.fetch)`。`await` 等待线程结果；`asyncio.to_thread` 是准确 API；参数必须是函数对象，不能添加括号提前调用。

第二次复测回答：能够写出 `await asyncio.to_thread(...)`，但将参数描述成“异步函数名”。

第二次复测反馈：`asyncio.to_thread()` 的用途是把同步阻塞函数放入线程执行，参数应是同步函数对象；异步函数本身应直接 `await`，不应交给 `to_thread()`。

状态：🟨

### 错题44

题目上下文：

```sql
CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC CHECK (price > 0),
    sku TEXT UNIQUE
);
```

按顺序尝试插入：

```text
A. id=1, name='Keyboard', price=99, sku='K001'
B. id=1, name='Mouse', price=30, sku='M001'
C. id=2, name=NULL, price=30, sku='M002'
D. id=3, name='Monitor', price=NULL, sku=NULL
E. id=4, name='Desk', price=-1, sku=NULL
F. id=5, name='Chair', price=50, sku=NULL
```

问题：哪些插入违反约束？普通 `UNIQUE` 和 `CHECK` 如何处理 `NULL`？

目前回答：B 的 ID 和 SKU 都重复；C 的 name 为空；D、E、F 的 SKU 为 NULL 因而失败；E 的 price 小于零。

标准回答：A 成功；B 只因 `id=1` 重复而失败，`M001` 与已有的 `K001` 不重复；C 因 `name` 违反 `NOT NULL` 而失败；D 成功，因为 `price` 没有 `NOT NULL`，`CHECK (NULL > 0)` 得到 UNKNOWN 并通过，而且普通 `UNIQUE` 默认允许多个 NULL；E 只因 `price=-1` 违反 CHECK 而失败，NULL SKU 本身允许；F 成功，第二个 NULL SKU 仍被允许。最终成功的是 A、D、F。

状态：🟨

### 错题45

题目上下文：

```text
两个 FastAPI Worker 同时查询 email 是否存在，都得到不存在，随后同时插入相同 email。数据库已设置 UNIQUE(email)。
```

问题：应用应如何处理其中一次插入触发的唯一约束冲突？

目前回答：通过 `try...finally` 处理冲突报错，也可以增加锁。

标准回答：使用 `try/except` 捕获数据库唯一约束异常，在事务失败后执行 `rollback`，再将可识别的 email 唯一冲突转换为业务冲突响应，例如 HTTP 409；`finally` 适合无论成功失败都执行的资源清理，不能按异常类型处理错误。数据库 UNIQUE 是最终防线，通常不应以应用内锁替代，尤其应用内锁无法跨 Worker。

状态：🟨

### 错题46

题目上下文：

```text
查询所有已支付且金额至少为 100 的订单，只返回 id、user_id、amount，先按金额降序，金额相同时按 ID 降序，只取前 10 条。
```

问题：如何正确编写 `ORDER BY`？

目前回答：`ORDER BY amount ASC, id ASC LIMIT 10`。

标准回答：应写 `ORDER BY amount DESC, id DESC LIMIT 10`。`ASC` 是升序，`DESC` 是降序；多列排序按书写顺序依次作为主排序键和相同值时的次排序键。

状态：🟨

### 错题47

题目上下文：

```text
统计每个用户已支付订单的数量和总金额，只保留已支付总金额至少为 250 的用户，并按总金额从高到低排序。
```

问题：如何正确组合 `WHERE`、`GROUP BY`、`HAVING` 和 `ORDER BY`？

目前回答：`SELECT user_id count(*) AS paid_count, sum(amount) AS all_amount FROM orders WHERE status='paid' HAVING sum(amount)>=250 ORDER BY amount DESC`。

标准回答：

```sql
SELECT
    user_id,
    COUNT(*) AS paid_count,
    SUM(amount) AS total_paid
FROM orders
WHERE status = 'paid'
GROUP BY user_id
HAVING SUM(amount) >= 250
ORDER BY total_paid DESC;
```

`user_id` 与 `COUNT(*)` 之间需要逗号；按用户聚合必须 `GROUP BY user_id`；`WHERE` 过滤原始 paid 行；`HAVING` 过滤聚合后的组；排序应使用 `SUM(amount)` 或别名 `total_paid`，不能在分组结果中直接使用未聚合的 `amount`。

状态：🟨

### 错题48

题目上下文：

```sql
SELECT SUM(amount)
FROM orders
WHERE user_id = 999;
```

问题：没有任何匹配行时结果是什么？如何返回 0？

目前回答：通常会报错，可以使用 `COALESCE`。

标准回答：查询不会因为空集而报错；`SUM(amount)` 在没有输入行时通常返回 `NULL`。若需要 0，应写 `COALESCE(SUM(amount), 0)`。`COUNT(*)` 是常见例外，空集时返回 0。

复测回答：能够正确判断 `COUNT(*)` 返回 0、`SUM(amount)` 返回 NULL，但忘记 `COALESCE` 名称。

状态：🟨

### 错题49

题目上下文：

```text
users(id, username)
orders(id, user_id, amount, status)

查询存在订单的用户及其订单，返回 username、订单 ID、amount、status；再使用 LEFT JOIN 查询所有用户及订单。
```

问题：多表查询时如何正确使用真实表名、列名和限定名？

目前回答：使用 `user_name`、`o.order_id`、`FROM users AS u JOIN order AS o`，并直接选择未限定的 `id`。

标准回答：应使用题目给出的真实标识符：`users`、`orders`、`username`、`orders.id`。多张表都含 `id` 时必须写 `u.id` 或 `o.id`，否则会产生列引用歧义。`order` 还是 SQL 关键字相关名称，应避免用作未引用的表名。示例：

```sql
SELECT
    u.username,
    o.id AS order_id,
    o.amount,
    o.status
FROM users AS u
JOIN orders AS o
    ON o.user_id = u.id;
```

状态：🟨

### 错题50

题目上下文：

```text
查询所有用户及其已支付订单数量，包括没有已支付订单的用户；没有已支付订单时数量必须是 0。
```

问题：应如何组合 `LEFT JOIN`、`ON`、`COUNT` 和 `GROUP BY`？

目前回答：使用普通 `JOIN`，未过滤 paid，也没有 `GROUP BY`：`SELECT id, user_name, count(o.id) ... JOIN order ...`。

标准回答：

```sql
SELECT
    u.id,
    u.username,
    COUNT(o.id) AS paid_order_count
FROM users AS u
LEFT JOIN orders AS o
    ON o.user_id = u.id
   AND o.status = 'paid'
GROUP BY
    u.id,
    u.username
ORDER BY u.id;
```

`LEFT JOIN` 保留没有订单的用户；paid 条件放在 `ON` 中避免过滤掉未匹配用户；`COUNT(o.id)` 忽略右表 NULL 并得到 0；按用户聚合需要 `GROUP BY`。

状态：🟨

### 错题51

题目上下文：

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

问题：未使用 `functools.wraps` 时，为什么可能影响 FastAPI？应该如何修复？

目前回答：装饰后 `__name__` 会变成 `wrapper`；不知道对 FastAPI 的具体影响；在 `wrapper` 上增加 `@wraps`。

标准回答：FastAPI 会通过函数签名分析 Path、Query、Body、类型注解和 `Depends`。未使用 `@wraps(func)` 时，框架和 `inspect.signature()` 可能只看到 `wrapper(*args, **kwargs)`，原函数的参数、注解和元数据被遮蔽，可能影响依赖解析和 OpenAPI。应在内部函数上添加 `@wraps(func)`；它会保留常用元数据，并通过 `__wrapped__` 让反射工具找到原函数。

状态：🟨

### 错题52

题目上下文：

```text
A. 普通用户资料列表查询
B. 一份事务内需要保持稳定数据视图的统计报告
C. 多个事务同时修改多行，并且必须维持复杂跨行规则

从 Read Committed、Repeatable Read、Serializable 中选择合理起点。
```

问题：三个场景分别更适合从哪个隔离级别开始考虑？

目前回答：A 使用 Repeatable Read，B 使用 Read Committed，C 使用 Serializable。

标准回答：A 通常从 PostgreSQL 默认的 Read Committed 开始，普通列表不要求同一事务多次查询始终看到相同快照；B 更适合 Repeatable Read，使事务内多次查询观察稳定快照；C 可以考虑 Serializable，使并发结果等价于某种串行顺序，但应用必须准备处理序列化失败并重试。隔离级别仍应结合真实一致性要求和并发代价选择。

状态：🟨

### 错题53

题目上下文：某张频繁更新的表中，`n_dead_tup` 持续升高，`last_autovacuum` 时间很近，同时存在一个两小时前开启且未结束的事务。

问题：优先怀疑什么问题？下一步应查看哪个系统视图？

目前回答：怀疑长事务造成表膨胀，但不知道下一步查看什么。

标准回答：优先怀疑长事务持有旧快照，拖住 `VACUUM` 的可移除边界，使部分旧行版本暂时无法清理。下一步查看 `pg_stat_activity`，重点关注 `xact_start`、`state`、`query` 等字段，定位长事务和 `idle in transaction` 会话；若进一步排查锁等待，可结合 `pg_locks`。

状态：🟨

### 错题54

题目上下文：

```sql
-- 事务 A
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;

-- 事务 B（事务 A 尚未结束）
a. SELECT * FROM accounts WHERE id = 1;
b. UPDATE accounts SET balance = 80 WHERE id = 1;
c. UPDATE accounts SET balance = 80 WHERE id = 2;
d. SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
```

问题：事务 B 的四种操作分别是通常立即执行，还是通常等待？

目前回答：a 立即执行；b、c、d 等待。

标准回答：a 通常立即执行；b 通常等待；c 通常立即执行；d 通常等待。`FOR UPDATE` 是针对被选中行的行级锁：它不会阻塞普通读取，但会阻塞其他事务修改或以冲突方式锁定同一行。事务 A 锁定 `id = 1`，并不影响事务 B 修改 `id = 2`。

状态：🟨

### 错题55

题目上下文：两个转账事务分别需要锁定账户 1 和账户 2。要求以统一顺序锁定两行，且把措施归类为“降低死锁概率”或“死锁后的恢复策略”。

问题：

```python
first_id = ...
second_id = ...
```

应如何根据 `from_id`、`to_id` 赋值？下面三项如何分类？

```text
a. 所有转账都按账户 ID 从小到大加锁
b. 捕获 deadlock 错误后，回滚并重试整个事务
c. 在事务内调用 30 秒的第三方接口
```

目前回答：`min(first_id, second_id)`、`max(first_id, second_id)`；a、b 是恢复策略；c 是降低概率。

标准回答：

```python
first_id = min(from_id, to_id)
second_id = max(from_id, to_id)
```

a 是降低死锁概率，因为所有事务按同一顺序获取锁，避免形成等待环；b 是死锁发生后的恢复策略，必须回滚并重试整个事务；c 既不是预防也不是恢复，反而会拉长持锁时间、增加锁等待和死锁风险。

状态：🟨

### 错题56

题目上下文：文档记录为 `id=1, version=3`。用户 A、B 同时读取；A 先提交，使版本变为 4。B 随后执行：

```sql
UPDATE documents
SET title = 'B 的修改', version = version + 1
WHERE id = 1 AND version = 3;
```

问题：B 的更新结果和服务层处理方式是什么？为什么 `WHERE` 中必须同时校验 `id` 与期望的 `version`？简单余额扣减更适合什么写法？

目前回答：更新 0 行后服务层重新执行；只按 id 更新会直接更新；余额扣减使用悲观锁。

标准回答：B 更新 0 行，表示读取到的版本已过期。服务层应把它当作并发冲突：通常返回“数据已更新，请刷新后重试”，或在明确安全的场景做有限次数、带退避的整操作重试；不能无条件自动重做旧意图。`id` 用于定位目标行，`version` 用于断言“它仍是我读取时的版本”；只按 `id` 更新会让 B 的旧编辑直接覆盖 A 的新编辑。简单扣余额可优先使用数据库原子条件更新，例如 `UPDATE accounts SET balance = balance - :amount WHERE id = :id AND balance >= :amount`，再根据受影响行数判断成功或余额不足；涉及多行/复杂读取校验时再考虑悲观锁。

状态：🟨

### 错题57

题目上下文：用户表有 `id`、`email`、`password_hash`、`is_active`。创建接口需要 `UserCreateDTO`，查询响应使用 `UserResponseDTO`，数据库读写使用 `UserORM`。

问题：`password`、`password_hash`、`email`、`id` 分别应该出现在哪些对象中？

目前回答：`password` 在 Create DTO 与 ORM；`password_hash` 在 ORM；`email` 在三者；`id` 在 Create DTO 与 ORM。

标准回答：`password` 只应由 Create DTO 接收，用来计算哈希后即不应持久化明文；`password_hash` 应在 ORM/数据库表，不应返回给客户端；`email` 通常会出现在 Create DTO、Response DTO、ORM；`id` 通常由数据库生成，因此会在 ORM 和 Response DTO 中，不应由普通创建 DTO 接收。DTO 按请求和响应的字段边界拆分，是安全边界而不是重复代码。

状态：🟨

### 错题58

题目上下文：Redis 缓存商品详情、库存及用户公开资料。商品详情和库存更新频率不同，详情缓存结构从 v1 升级到 v2。

问题：为什么详情和库存应拆分 Key？`detail:v1` 与 `detail:v2` 同时存在解决什么问题？设计“用户 1001 的公开资料缓存”的 Key。

目前回答：详情和库存拆分是因为更新频率不同；版本并存是不直接覆盖旧内容和缓存时间；写成了包含 `SET` 和 JSON 值的 `cache:user:public:msg:1001:v1`。

标准回答：拆分 Key 的直接收益是两类数据可以独立设置 TTL、独立删除/回填，库存变动不必让稳定的详情缓存也失效。`v1` 与 `v2` 并存用于缓存数据结构迁移：新代码读取 v2，旧 Key 可等待 TTL 到期或再统一删除，避免新旧代码/新旧数据格式混用。所需的 Key 是 `cache:user:1001:profile:v1`；Key 设计题只写 Key 名，不需要 `SET` 命令或 Value JSON。

状态：🟨

### 错题59

题目上下文：账户余额为 100，两个事务都读取余额后尝试扣除 80；后端同时存在简单扣款和复杂多行资金协调场景。

问题：应用层先计算后覆盖写入会有什么问题？简单扣款的原子更新思路是什么？什么时候更需要 `SELECT ... FOR UPDATE`？

目前回答：可能读取到不是最新余额后覆盖另一个事务的更新；不会写原子更新；两个事务并发时更需要锁。

标准回答：应用层先读、计算新余额、再覆盖写入可能造成丢失更新，甚至让两次扣款都基于旧余额通过校验。简单扣款优先使用数据库原子条件更新：在数据库内执行 `balance = balance - amount`，并附加 `balance >= amount` 条件，再根据受影响行数判断成功、余额不足或账户不存在。并发本身不自动意味着必须悲观锁；当业务需要先读取后进行复杂校验、协调多行/多表状态，且这些判断必须在事务期间保持一致时，才更可能使用 `SELECT ... FOR UPDATE`。

状态：🟨

### 错题60

题目上下文：

```python
class ProductUpdateDTO(BaseModel):
    name: str | None = None
    price: int | None = None
```

问题：请求 `{"price": 0}` 在无额外约束时是否能通过？若价格必须大于 0，应怎样声明？为什么“价格 > 0”适合 DTO，而数据库中是否存在同名商品通常不适合 Pydantic 验证器？

目前回答：无约束时能通过；约束写成 `de=0`；同名查询涉及 I/O，验证器可能被多次调用。

标准回答：无额外约束时 `0` 是合法 `int`，因此能通过。使用 `price: int | None = Field(default=None, gt=0)` 声明大于 0。数值范围是纯输入校验，适合 DTO；同名查询需要数据库 I/O，还可能有并发竞态，应该由 Service/Repository 协调并依赖数据库 UNIQUE 约束作为最终防线，而不是放在 Pydantic 验证器。

状态：🟨

### 错题61

题目上下文：逻辑过期实验中，单个 FastAPI 进程使用 `asyncio.Lock()` 确保同一时刻只有一个后台任务刷新热点缓存；生产环境可能部署多个 Uvicorn worker 或多个应用实例。

问题：`asyncio.Lock()` 是否足以让所有 worker/实例只刷新一次？跨进程应使用什么锁？

目前回答：不够；多进程、多实例无法访问这个进程中的锁；不知道应换成什么锁。

标准回答：`asyncio.Lock()` 只存在于单个 Python 进程的内存中，无法协调其他 worker 或机器。跨进程/多实例应使用共享协调器上的分布式锁，当前栈最常见是 Redis 锁：用 `SET lock:key <唯一token> NX EX <seconds>` 原子抢锁，并仅由持有对应 token 的一方释放锁。这样所有实例看到同一把锁；后续第 9 章第 5 趴会专门实操其超时、续期和安全释放边界。

状态：🟨

### 错题62

题目上下文：缓存重建使用 Redis 锁 `SET lock:key token NX EX 5`。A 成功抢到锁后，重建数据源耗时可能超过 5 秒；同时另一个请求 B 在等待。

问题：没有 `EX` 的后果是什么？锁租期短于实际重建时间时，具体会发生什么？

目前回答：没有 `EX` 时 A 会一直占锁；有 `EX 5` 的代价是如果数据源查询超过 5 秒，锁就没有意义。

标准回答：没有 `EX` 时，A 若崩溃，锁可能永久存在，其他请求持续无法重建。`EX 5` 能避免永久锁，但若 A 的重建超过 5 秒，锁会在 A 尚未完成时过期，B 可能重新抢到锁并也开始重建，互斥效果被破坏。唯一 token + 比对后再删除仍能避免 A 误删 B 的新锁，但不能阻止两次重建；应让租期覆盖预期最长耗时，或在确有必要时使用带安全续期的锁，并设置回源超时。

状态：🟨

### 错题63

题目上下文：PostgreSQL 中事务 A、B 反向锁定两行而发生死锁，数据库选择其中一个事务作为受害者并回滚。

问题：为什么通常必须从头重试整个事务，而不能只重试最后一条 SQL？

目前回答：因为会 rollback，当前事务拿到的数据可能会是“错峰”。

标准回答：死锁受害事务已被完整回滚，之前的读取、校验、局部写入和持有锁全部失效；等待期间其他事务还可能改变业务前提。只重试最后一条 SQL 会脱离原有的读取/校验上下文，可能导致错误决策。因此应从 `BEGIN` 起重新读取、重新校验并重新执行整个事务；同时设置有限次数重试和退避，避免持续冲突。

状态：🟨

### 错题64

题目上下文：热点缓存重建使用 5 秒 Redis 锁，但数据源通常 200ms、偶发卡住 20 秒；需要决定锁和回源 I/O 的保护策略。

问题：固定把锁租期调为 30 秒有什么代价？除锁租期外，回源请求还应配置什么？为什么重建写缓存应尽量幂等？

目前回答：锁会存在太久，失败后下一次重建等待很久；应设置最大查询时间和查询数；写缓存只需关注同一 Key 写什么内容。

标准回答：租期过长会使崩溃或卡住后的锁长期占用，其他请求只能等待或失败，降低可用性。应为单次数据库/HTTP 回源设置明确 timeout（并限制重试），避免临界区无限卡住；“查询数”不能替代一次 I/O 的超时。重建操作应尽量幂等：相同 Key 用来自权威数据源的等价结果重复 `SET`，最终仍收敛到正确缓存状态；若不同版本可能乱序覆盖，还需要版本号或条件写入等额外保护。

状态：🟨

### 错题65

题目上下文：账户 `id=1` 当前余额 100，两个并发请求都执行：`UPDATE accounts SET balance = balance - 80 WHERE id = 1 AND balance >= 80`。

问题：为什么两个请求不会都成功扣款？

目前回答：因为 `UPDATE accounts` 增加了行锁。

标准回答：`UPDATE` 确实会对目标行产生并发写入协调，但仅说“有行锁”不完整。第一个事务成功把余额更新为 20；另一个事务等待后，在可继续执行时会基于最新可见行版本重新检查 `WHERE balance >= 80`，条件不再满足，因此影响行数为 0。原子条件更新把“余额校验 + 扣减”放进同一条数据库操作，避免两个应用层旧读都通过后再覆盖写入。

状态：🟨

### 错题66

题目上下文：教学版 FastAPI 通过 `asyncio.create_task()` 执行解析任务，任务进度写入 Redis Hash；应用在进度 50% 时重启。

问题：Redis 中任务状态会自动变成什么？生产环境怎样改善？

目前回答：会变成 `failed`；生产若支持断点续跑则继续，否则可先设为 `queued` 后重新执行。

标准回答：进程被终止时，内存中的协程直接中断，代码不会自动把 Redis 状态改为 `failed`，Hash 往往会遗留为 `running` 直到 TTL 过期。生产中应由独立 Worker/任务队列执行，并设置任务租约、心跳或超时扫描：长期无心跳的 `running` 任务可被标记为失败或按安全的幂等策略重新投递。不能不加判断地把所有任务改回 `queued`，否则非幂等任务可能重复执行。

状态：🟨

### 错题67

题目上下文：

```python
def make_counter():
    count = 0
    def increment():
        count += 1
        return count
    return increment
```

问题：调用 `counter = make_counter(); counter()` 会报什么错误？为什么？如何最小改动修复？

目前回答：错误类型和原因忘记；可以使用 `local`。

标准回答：会报 `UnboundLocalError: cannot access local variable 'count' where it is not associated with a value`。函数体内出现 `count += 1` 等同于对 `count` 赋值，因此 Python 在编译函数时将 `count` 判定为 `increment` 的局部变量；但右侧 `count` 在该局部作用域尚未赋值就被读取。应在 `increment` 内声明 `nonlocal count`，表示重新绑定最近一层外部函数 `make_counter` 的 `count`。`local` 不是 Python 的这个关键字，且局部变量正是导致错误的原因。

状态：🟨

### 错题68

题目上下文：业务代码拿到一个生成器对象，需要解释它为什么通常只能遍历一次，并为“需要两次独立遍历同一批数据”选择策略。

问题：生成器为何只能遍历一次？何时保留原始可迭代对象、重新创建生成器或缓存为列表？

目前回答：原因不清楚；会缓存成列表，因为需要两次独立遍历。

标准回答：生成器也是迭代器，内部保存当前位置；每次 `next()` 或 `for` 都从当前位置向后推进，耗尽后抛出 `StopIteration`，不会自动回到开头。若原始数据是可重复迭代对象（如 list），应保留它并每次调用 `iter(values)` 得到独立迭代器；若有无副作用、可重跑的生成器工厂，应每次重新调用工厂创建新生成器；若来源是一次性流、读取昂贵且数据量可控，可用 `list()` 物化后多次遍历。缓存列表会增加内存占用，不应无条件使用。

状态：🟨

### 错题69

题目上下文：FastAPI + SQLAlchemy 异步项目中，`Engine` 作为应用级对象，`AsyncSession` 通过 Dependency 为请求创建。

问题：为什么 Engine 可共享，而 AsyncSession 不应作为全局单例供并发请求共用？

目前回答：Engine 创建成本大，适合全局共享；AsyncSession 每个并发请求创建一次，主要是全局创建可能过期且不方便管理。

标准回答：Engine 管理数据库连接池，创建成本高且设计为应用级复用。AsyncSession 是一次工作单元，内部包含事务状态、待 flush 的对象、Identity Map 等可变状态，不能安全地被多个并发请求共享；共享会让不同请求的查询结果、提交/回滚与待写入对象相互串扰。Session 关闭后连接归还池，重点不是“Session 过期”。

状态：🟨

### 错题70

题目上下文：`architecture_users.email` 有数据库 UNIQUE 约束，Service 创建用户时可先通过 Repository 查询是否已有同邮箱记录。

问题：已有 UNIQUE 后是否仍应先查询？各自承担什么责任？

目前回答：需要先查；UNIQUE 只能判断唯一，无法区分是否已经存在。

标准回答：预查询是可选的，常用于尽早给出友好的“邮箱已存在”业务提示；但它不能保证并发正确性，因为两个请求可能同时查到不存在。数据库 UNIQUE 才是最终约束，Service 必须捕获插入时的 `IntegrityError` 并转换为冲突结果。UNIQUE 正是用于防止相同邮箱重复存在。

状态：🟨

### 错题71

题目上下文：Alembic 已执行首个 `20261008_01_create_architecture_users` 迁移，之后新增 `architecture_user_settings` 表。

问题：为什么应新增第二个 migration，而不是修改已经执行过的第一个 migration？

目前回答：不知道。

标准回答：已执行 migration 是共享的数据库历史：本地、测试、预发布和生产可能已经处在该版本。修改旧 migration 会让“同一个 revision 名称”在不同环境代表不同 schema，部署时无法可靠判断该执行什么变更。新 schema 变化应写成新的、按顺序执行的 migration，数据库 `alembic_version` 记录当前版本；这样可以 review、部署、追溯，也能在设计允许时执行 downgrade。开发早期尚未共享的本地 migration 可以重写，但一旦被其他环境应用，就视为不可变历史。

状态：🟨

### 错题72

题目上下文：FastAPI 路由声明 `@router.get("/{user_id}")`，参数为 `user_id: int`；客户端请求 `GET /users/abc`。

问题：应返回 404 还是 422？路由函数与 `UserService.get_user()` 是否执行？

目前回答：404；不会执行，因为前置直接抛出异常。

标准回答：返回 `422 Unprocessable Content`，因为 `abc` 无法通过 FastAPI/Pydantic 的路径参数 `int` 校验。路由函数和 `UserService.get_user()` 不会执行，因为还没有得到合法的 `user_id`；404 只用于参数格式合法、但数据库中没有对应用户的情况，例如 `/users/999999`。

状态：🟨

### 错题73

题目上下文：`UserService` 抛出 `EmailAlreadyExistsError`，应用注册了统一异常处理器，将其转为 HTTP `409 Conflict`。

问题：将领域异常映射成 HTTP 409 应放在 Repository、Service，还是接口边缘层？为什么？

目前回答：应放在 Service，因为 Repository 不应处理异常，业务层更适合处理。

标准回答：Service 应负责识别并抛出不含 HTTP 细节的领域异常，例如 `EmailAlreadyExistsError`；Repository 只处理数据访问。将该异常映射为 HTTP 409、JSON 响应格式的工作属于接口边缘层，即 FastAPI 的 Exception Handler。这样同一 Service 才能被 Worker、CLI、测试或其他传输协议复用，而不携带 HTTP 状态码耦合。

状态：🟨

### 错题74

题目上下文：为 `POST /users` 写接口测试，希望验证路由的 HTTP 入参、响应 DTO 与状态码，但不连接真实 PostgreSQL。当前路由通过 `Depends(get_user_service)` 获得 `UserService`。

问题：最适合在测试中替换 Router、`get_user_service` 依赖装配函数、`UserService` 内部业务代码，还是 FastAPI 本身？

目前回答：替换 `UserService` 内部业务代码。

标准回答：对于“路由接口测试”，应替换 `get_user_service` 这个依赖装配函数（FastAPI 的 `app.dependency_overrides`）。测试便能注入假的 Service，而 Router、请求校验、HTTP 状态码和响应模型仍保持真实运行。若目标是单独测试 Service 的业务规则，则不应改写 Service 本身，而应为它注入假的 Repository/Session；不同测试层替换不同的外部依赖。

状态：🟨

### 错题75

题目上下文：查询“用户 ID 为 42 的详情”，`id` 是数据库主键；路由要求“参数合法但用户不存在”时返回 HTTP 404。Repository 与 Service 分层。

问题：Repository 查询主键时应直接抛“用户不存在”异常，还是返回什么？Service 如何处理？

目前回答：可以用 `scalar_one()` 或 `scalar_one_or_none()`；不存在时抛异常，或返回 `None` 后处理成 404。

标准回答：主键查询适合 `session.get(UserORM, user_id)`，或用 `scalar_one_or_none()`；Repository 返回 `UserORM | None`。查不到记录通常是正常数据访问结果，不应由 Repository 抛 HTTP 404 或把 `NoResultFound` 当业务流程；Service 看到 `None` 后抛 `UserNotFoundError`，最终 Exception Handler 映射为 HTTP 404。`scalar_one()` 要求“必定恰好一条”，不适合预期允许不存在的用户详情查询。

状态：🟨

### 错题76

题目上下文：路由声明 `GET /users`，`limit` 参数为 `Query(ge=1, le=100)`；客户端请求 `GET /users?limit=101`。

问题：会返回什么？Router 函数体、Service、Repository 是否执行？

目前回答：Router 参数校验后会调用 Service，再由 Repository 执行数据库操作。

标准回答：FastAPI 会在调用路由函数体前完成查询参数校验。`101` 不满足 `le=100`，因此直接返回 `422 Unprocessable Content`；虽已完成路由匹配，但 `list_users()` 路由函数体、Service 和 Repository 都不会执行，也不会访问数据库。只有参数合法时才会进入业务调用链。

状态：🟨

### 错题77

题目上下文：PostgreSQL 默认隔离级别为 `Read Committed`。列表接口先执行当前页 `SELECT ... LIMIT/OFFSET`，随后执行 `SELECT count(*)`；两条 SQL 之间，另一事务新增并提交了一条符合筛选条件的记录。

问题：`items` 与 `total` 是否一定来自同一数据快照？为什么？

目前回答：是；若不是同一快照会造成数据误差，例如 `items` 与 `total` 对不上。

标准回答：不一定。`Read Committed` 会让每条 SQL 在开始时取得新的语句级快照：第一页查询可能没看到新记录，随后执行的 `count(*)` 可能已看到它，因此 `items` 与 `total` 可以暂时不完全一致。很多普通后台分页可接受这种短暂偏差；若业务确实需要同一快照，需在同一事务中使用适当隔离语义，并评估并发与性能代价。

状态：🟨

### 错题78

题目上下文：取消 Agent 任务时，Repository 读到 `TaskORM(status="succeeded")`；Service 构造领域对象并调用 `AgentTask.request_cancel()`，得到 `InvalidTaskTransitionError`。HTTP 接口应对客户端返回 `409 Conflict`。

问题：哪一层应将该异常映射为 HTTP 409？为什么领域模型与 Repository 不应直接返回 409？

目前回答：Service 结合 Router 转换相关异常，Router 返回 409。

标准回答：领域模型只抛出不含 HTTP 细节的状态转换异常；Service 可以让它向上传播，或转为更明确的领域异常，但不应依赖 HTTP 409。由 FastAPI 的统一 Exception Handler 这个接口边缘层将领域异常映射为 HTTP 409 与 JSON 错误体，避免每个 Router 重复 `try/except`。Repository 只提供数据库事实，也不知道“已完成任务不可取消”是否应对 HTTP 客户端表现为 409、对 Worker 表现为跳过，还是触发其他补偿。

状态：🟨

### 第9章 第5趴：分布式锁

阶段：已学

目标：理解并实操跨 worker/实例的 Redis 分布式锁，能判断锁的适用范围与安全边界。

实验 15 完成：在 FastAPI 热点缓存重建接口中使用 `SET key token NX EX` 抢锁，并发发出 10 个请求后验证数据源读取计数为 1；未抢到锁的请求等待缓存回填后读取，不直接并发回源。

实验 16 完成：理解唯一 token 与 Lua 比对删除的必要性：锁过期并被下一请求接管后，旧持锁者不能无条件删除新锁。能够说明 `EX` 防永久锁、但租期不足会造成重复重建；需要以回源 timeout、有限等待和幂等写入共同控制风险。

第 5 趴回顾：Redis 锁用于短时、跨进程/实例的协调，例如热点缓存单飞重建；`asyncio.Lock()` 只能保护单个 Python 进程。Redis 锁不能替代数据库事务：简单余额扣减优先原子条件更新，复杂一致性协调才在事务内采用行锁；长任务不应长期持 Redis 锁，应使用队列或专门任务协调。

### 第9章 第6趴：限流、Session 与任务状态

阶段：已学

目标：在 FastAPI 中用 Redis 落地访问限流、登录态识别与异步任务进度查询，并能区分三类 Key 的职责。

实验 17 完成：实现并验证固定窗口限流：Lua 将 `INCR` 与首次 `EXPIRE` 原子化；同一 client 在 10 秒内第 4 次请求返回 `429` 与 `Retry-After`。理解限流身份必须来自可信 `current_user.id` 或受控 IP 维度，而非前端任意参数。

实验 18 完成：实现并验证 Redis Session 独立 FastAPI 示例 `session_lab.py`：登录生成随机 session_id，Redis Hash 保存用户映射与 TTL，Cookie 使用 HttpOnly / SameSite；认证 Dependency 从 Cookie 查询 Session；注销同时删除 Redis Session 和 Cookie。知道生产 HTTPS 必须启用 Secure Cookie。

实验 19 完成：实现并验证独立任务状态示例 `task_status_lab.py`：创建接口返回 `202 + job_id`，Redis Hash 记录 `queued → running → succeeded/failed` 与进度，查询接口按 job_id 返回状态。理解进程内 `asyncio.create_task()` 仅适合教学；生产应使用独立 Worker/任务队列、心跳或租约来处理重启遗留的 running 任务。

实验 20 完成：实现并验证独立滑动窗口示例 `sliding_window_rate_limit_lab.py`：用 ZSet 保存请求时间戳，Lua 原子完成清理、计数和写入；理解相对固定窗口更平滑，但每个请求占用一条记录，内存与操作成本更高。

第 6 趴回顾：`session:{id}` 回答“你是谁”，`rate_limit:{interface}:{subject}` 回答“这次能不能进入”，`task:job:{id}` 回答“已接收任务进行到哪里”。常用状态码：Session 缺失/失效 `401`，权限不足 `403`，限流 `429`，任务不存在 `404`，异步任务已接收 `202`，参数校验失败 `422`。PATCH 更新必须使用 `model_dump(exclude_unset=True)`，以免未传字段被默认 `None` 覆盖。

### 第9章 第7趴：持久化与高可用基础

阶段：已学

目标：理解 Redis 内存数据的持久化恢复边界，以及主从复制与故障切换如何降低服务中断。

实验 21 完成：检查当前 Docker Redis 配置，确认 `appendonly=yes`、`appendfsync=everysec` 且配置了 RDB `save` 规则；理解 RDB 是定期快照，AOF 是追加写命令日志。

实验 22 完成：写入专用 Key 后正常重启 Redis 容器，验证其仍可读取。能说明这只证明持久化恢复有效，不能证明机器断电时不会丢失最近写入；`everysec` 在极端故障下仍可能丢失约 1 秒写入。

实验 23 完成：通过 `INFO replication` 确认学习环境是单 Primary、0 Replica。理解持久化不等于高可用；高可用需要副本与 Sentinel 故障检测/切换，且异步复制下尚未同步至副本的最后写入仍可能在主故障后丢失。

第 7 趴回顾：RDB 偏向紧凑快照与备份，AOF 偏向较低 RPO；关键订单、余额等事实仍以 PostgreSQL 事务为最终真相来源。Redis 的主从/Sentinel 降低故障恢复时间，但不自动提供事务级强一致性。

## 当前 Top5

1.  Python对象与引用 ⭐⭐⭐
2.  可变对象 vs 不可变对象 ⭐⭐⭐
3.  == 与 is ⭐⭐⭐
4.  默认参数为什么不能使用 \[\] ⭐⭐⭐
5.  深浅拷贝 ⭐⭐⭐

## 已完成

### 第1章 第2趴：可变默认参数

已掌握：

- 默认参数中的可变对象会被多次调用共享
- 多个变量引用同一可变对象时，一处修改会被其他引用观察到
- 使用 `None` 作为默认值，并在函数内部创建新列表
- 理解显式传入列表时，函数仍会操作调用方提供的同一个对象
- 如果不允许修改调用方列表，应先复制再修改

需要加强：

- 默认参数是在函数定义时求值一次
- 按实际 print 时刻判断共享对象的最终状态
- 使用“对象引用”而不是“地址”描述 Python 语义

阶段：已学

## 已完成补充

### 第1章 第3趴：浅拷贝与嵌套可变对象

目标：理解复制外层容器不等于复制其中的所有嵌套对象。

当前掌握：

- 浅拷贝创建新的外层容器
- 嵌套可变对象仍可能被共享
- 完全隔离嵌套对象可使用递归深拷贝
- 能区分给字典键重新赋值与原地修改嵌套列表

需要加强：浅拷贝复制的是元素引用，不是“重新创建第一层不可变数据”；区分修改容器绑定与修改被引用对象。

阶段：已学

## 已完成补充

### 第1章 第4趴：函数参数传递

目标：理解 Python 函数调用中的对象共享传递，以及形参重新绑定与修改实参对象的区别。

掌握：

- Python 函数调用采用对象共享传递（call by sharing）
- 形参与实参开始时引用同一个对象
- 形参重新绑定不会改变外部变量的绑定
- 通过形参原地修改可变对象会被外部观察到

阶段：已学

## 已完成补充

### 第1章 第5趴：参数类型与解包

目标：掌握位置参数、关键字参数、默认参数、`*args`、`**kwargs` 及调用时解包。

当前掌握：普通参数、默认参数、`*args` 收集为元组、`**kwargs` 收集为字典。

需要加强：无额外参数时 `*args` 是空元组、`**kwargs` 是空字典；区分位置参数与关键字参数；理解 `*` 与 `**` 在函数定义和调用位置的不同作用。

新增掌握：

- 调用处 `*sequence` 将序列展开为位置参数
- 调用处 `**mapping` 将字典键值展开为关键字参数
- 能解释列表元素按顺序匹配普通形参

阶段：已学

## 已完成补充

### 第1章 第6趴：仅位置与仅关键字参数

目标：理解 `/` 和 `*` 在函数签名中的参数边界，以及清晰 API 设计中的用途。

掌握：

- `/` 左侧是仅位置参数
- `*` 右侧是仅关键字参数
- 能判断错误调用违反的是哪一侧规则

阶段：已学

## 已完成补充

### 第1章 第7趴：作用域与 LEGB

目标：掌握 Local、Enclosing、Global、Built-in 的名称查找顺序，以及赋值对局部作用域的影响。

当前掌握：能判断函数内赋值导致名称成为局部名称；知道使用 `global` 修改模块级名称。

需要加强：准确说出 `UnboundLocalError`；理解 `global` 与 `nonlocal` 分别指向 Global 和 Enclosing 作用域。

新增掌握：

- `nonlocal` 修改最近一层外部函数作用域中的名称
- `global` 修改模块全局作用域中的名称
- 能准确推导嵌套函数多次调用后的状态变化

阶段：已学

## 已完成补充

### 第1章 第8趴：一等函数与闭包

目标：理解函数可以作为对象传递和返回，以及闭包如何保留外部函数状态，为装饰器和依赖注入打基础。

当前掌握：函数可以赋值给变量和作为返回值；能区分返回函数对象与调用函数后返回结果。

需要加强：准确描述闭包“捕获外层作用域的名称绑定”；分清外层函数返回内部函数与随后调用内部函数两个阶段。

新增掌握：

- 每次调用外层函数会创建相互独立的闭包状态
- `nonlocal` 可更新闭包捕获的外层绑定
- 能解释有状态闭包为何影响后续调用结果

阶段：已学

## 已完成补充

### 第2章 第1趴：装饰器基础

目标：理解装饰器本质是接收函数并返回新函数，以及 `@decorator` 的语法糖展开形式。

当前掌握：装饰器可在原函数调用前后增加行为；装饰器内部不返回结果时外部得到 `None`。

需要加强：`@decorator` 展开为重新绑定函数对象；区分函数定义后的装饰阶段与运行时调用阶段；装饰后的名称首先调用包装函数。

新增掌握：

- 装饰器在被装饰函数定义完成后立即应用
- 装饰后的函数名称引用包装函数
- 包装函数通过闭包保留原函数对象
- 能准确推导装饰阶段与调用阶段的输出顺序

阶段：已学

## 已完成补充

### 第2章 第2趴：functools.wraps

目标：理解普通装饰器会丢失原函数元数据，以及 `@wraps(func)` 如何保留名称、文档和签名相关信息。

当前掌握：知道 `@wraps(func)` 可保留原函数名称和文档；删除后名称变成 `wrapper`、文档通常为 `None`。

需要加强：读取函数属性不会执行函数；`wraps` 不改变调用顺序；外层装饰器在定义阶段执行；装饰阶段创建包装函数不等于执行其函数体，包装函数体只在调用阶段执行。

新增掌握：

- 读取函数属性不触发函数调用
- `@wraps(func)` 保留原函数名称和文档等元数据
- 能区分创建包装函数对象与执行包装函数体

阶段：已学

独立总结代码：`02_装饰器_functools_wraps.py`

## 下一趴

### 第2章 第3趴：带参数装饰器

目标：理解三层嵌套结构及 `@decorator(config)` 的展开过程。

阶段：已学

掌握：三层函数分别接收配置参数、原函数和调用参数；能展开 `func = decorator(config)(func)`；理解循环中返回最后一次调用结果。

需要复习：按循环次数写全副作用输出，并检查最外层 `print` 是否还会打印返回值。

### 第2章 第4趴：多装饰器叠加

阶段：已学

目标：理解多个装饰器自下而上应用、调用时自上而下进入的顺序。

掌握：装饰器自下而上应用；调用从最外层进入；返回阶段从最内层逐层向外；任一层遗漏返回值会使外层最终得到 `None`。

需要复习：逐字核对原函数返回值，避免把 `100` 写成 `10`。

### 第2章 第5趴：可迭代对象与迭代器

阶段：已学

目标：区分 iterable 与 iterator，掌握 `iter()`、`next()`、`StopIteration` 以及 for 循环的底层协议。

当前掌握：可迭代对象通过 `iter()` 产生迭代器；迭代器保存遍历位置；for 循环会继续使用当前迭代位置；`__next__()` 通过 `StopIteration` 通知结束。

需要加强：`list(iterator)` 会消耗迭代器而不只是查看内容；同一迭代器耗尽后不会自动重置。准确描述为“迭代器已耗尽，继续调用 `next()` 会抛出 `StopIteration`”，而不是“迭代器处于 StopIteration”。迭代器自身也是可迭代对象。

新增掌握：同一个可迭代对象可产生多个相互独立的迭代器；`iter(list) is iter(list)` 为 `False`；迭代器的 `iter(iterator)` 通常返回自身。

### 第2章 第6趴：生成器与 yield

阶段：已学

目标：理解生成器是特殊迭代器，掌握惰性执行、暂停与恢复、耗尽行为及其内存优势。

当前掌握：生成器函数调用只创建对象；第一次 `next()` 才启动；`yield` 产出并暂停；下一次从 `yield` 后恢复；函数结束时通过 `StopIteration` 通知结束；for 自动捕获结束信号。

需要加强：描述暂停点时说“在当前 `yield` 产出后暂停，下一次从其后恢复”；继续学习惰性计算、一次性消费和内存优势。

总结：生成器是特殊迭代器；函数调用只创建生成器对象；`next()` 驱动执行；`yield` 产出并暂停；耗尽后不会自动重置；适合大数据、文件、数据库和流式响应。

### 第2章 第7趴：上下文管理器

阶段：已学

目标：理解 `with`、`__enter__`、`__exit__` 与资源释放，并衔接 `contextlib.contextmanager` 和 FastAPI 的 `yield` 依赖。

当前掌握：`__enter__` 的返回值绑定给 `as` 后的名称；退出 with 时执行 `__exit__`；返回 `True` 抑制异常，返回 `False`/`None` 使异常继续传播。

需要加强：区分 `exc_type`（异常类型）、`exc_value`（异常实例及消息）和 traceback；区分上下文管理器清理资源、内部抑制异常与外层 `except` 捕获异常；`finally` 只保证执行，不会自动吞掉由 `raise` 传播的异常。

新增掌握：生成器上下文管理器在进入 with 时执行 yield 前代码；异常会在 yield 位置重新进入生成器；finally 负责资源清理；内部重新 raise 后可由外层 except 最终处理。

### 第3章 第1趴：同步、异步与协程

阶段：已学

目标：理解 `async def` 调用返回协程对象、`await` 的暂停语义，以及事件循环如何调度 I/O 并发。

当前掌握：调用 `async def` 返回协程对象而不立即运行函数体；`await` 开始驱动并等待协程；能准确推导单协程执行顺序。

需要加强：`asyncio.sleep(0)` 的核心作用是让出执行权，不是实际延迟；`await` 获取的是协程 `return` 的结果；`async def` 不等于自动并发，协作式切换依赖可暂停的 `await`。

新增掌握：协程对象只是待执行的异步计算；`create_task()` 会将协程包装为 Task 并安排运行；Task 不会抢占当前代码，要等事件循环重新获得控制权。

### 第3章 第2趴：Task、gather 与并发耗时

阶段：已学

目标：掌握串行 await 与并发调度的耗时差异、gather 返回值顺序、Task 结果和异常传播。

当前掌握：提前创建多个 Task 可形成并发；总耗时接近最长任务而非耗时之和；任务完成顺序可与结果收集顺序不同。

需要加强：Task 对象保存状态、结果或异常；`await task` 返回的是协程的 return 值，而不是包含所有 Task 信息的复合对象；区分 gather 不自动取消其他任务与 asyncio.run 关闭事件循环时取消剩余任务。

新增掌握：`wait_for` 可限制等待时间；超时会取消内部任务；取消时仍执行 finally 清理；外层可捕获超时后继续运行。

需要继续加强：取消由 wait_for 发起，但 `CancelledError` 在协程当前暂停的 await 处进入；捕获后重新 raise 是为保留取消语义。

### 第3章 第3趴：阻塞代码与事件循环

阶段：已学

目标：区分同步阻塞调用与异步等待，掌握 `asyncio.to_thread()` 的适用场景，并理解 I/O 密集与 CPU 密集任务的处理方式。

当前掌握：`async def` 不会自动把 `time.sleep` 等同步调用改造成异步；同步阻塞调用会暂停整个事件循环；同步 I/O 可考虑 `asyncio.to_thread()`。

需要加强：一旦事件循环线程被同步函数阻塞，其他协程连开始执行的机会都没有，必须等阻塞调用返回。

新增掌握：gather 只是安排并发任务，不表示同时并行；asyncio 默认单线程协作式调度；同步阻塞调用不让出控制权；`asyncio.to_thread()` 可把同步阻塞 I/O 放到工作线程。

### 第3章 第4趴：协程、线程与进程

阶段：已学

目标：区分并发与并行、I/O 密集与 CPU 密集任务，并能为 FastAPI/Agent 后端选择协程、线程池、进程池或独立 Worker。

掌握：原生异步 I/O 使用协程；同步阻塞 I/O 使用线程；纯 Python CPU 密集任务使用进程或独立 Worker；`async def` 不会把同步或 CPU 密集代码自动改造成异步。

需要复习：任务类型取决于当前服务是在等待远程结果还是本地执行计算；异步数据库驱动通常使用协程和连接池，不需要额外线程。

### 第3章 第5趴：异步竞态与同步原语

阶段：已学

目标：理解协程在 await 处交错造成的竞态条件，掌握 `asyncio.Lock` 与 `Semaphore` 的用途。

掌握：单线程协程也可能因 await 交错产生竞态；Lock 保护共享状态；Semaphore 限制并发数量；临界区应尽量小，避免长时间持锁等待 I/O。

需要复习：不同协程的局部变量彼此独立，但可能保存同一共享状态的旧快照，从而发生丢失更新。

### 第3章 第6趴：异步队列与背压

阶段：已学

目标：掌握 `asyncio.Queue`、生产者/消费者、`task_done()`、`join()` 与有界队列背压。

当前掌握：`get()` 表示领取任务，`task_done()` 表示处理结束；`join()` 等待未完成计数归零；遗漏 `task_done()` 会导致 join 持续等待；消费者需要循环才能持续处理任务。

新增掌握：使用哨兵结束消费者；哨兵也需要 task_done；多个消费者通常需要多个哨兵；有界队列通过暂停生产者形成背压。

需要加强：使用“入队/出队”而不是“进栈/出栈”；`asyncio.Queue` 默认是 FIFO，最早放入的元素最先取出。

### 第3章 第7趴：异步综合练习与面试

阶段：已学

目标：综合使用 Task、gather、超时、Semaphore、Queue 与异常处理，形成可用于 FastAPI/Agent 后端的异步设计能力。

掌握：Semaphore 限制并发名额；wait_for 控制单任务超时；内部捕获可将失败转换为受控结果；gather 按输入顺序返回；退出 async with 时释放并发名额。

### 第4章 第1趴：HTTP 请求、响应与状态码

阶段：已学

目标：从后端视角理解 HTTP 请求/响应结构、方法语义、状态码分类与 RESTful API 的基本约定。

掌握：请求与响应结构；GET/POST/PUT/PATCH/DELETE 语义；幂等性；2xx/4xx/5xx 分类；200、201、204、401、403、404、409、422、429、504 的使用场景。

### 第4章 第2趴：创建 FastAPI 应用与 Uvicorn

阶段：已学

目标：理解 FastAPI 应用对象、路径操作注册、ASGI 与 Uvicorn 启动命令，并运行第一个健康检查接口。

掌握：FastAPI 应用对象；路由装饰器注册；Uvicorn 与 ASGI 的职责；`module:app` 启动语法；默认 `/docs` 与 `/openapi.json`；导入模块时注册路由但不调用处理函数。

需要复习：路径存在但方法不支持是 405；路径不存在是 404；响应体应能准确写出序列化后的 JSON。

### 第4章 第3趴：路由与 RESTful 设计

阶段：已学

目标：使用资源名、HTTP 方法和状态码设计清晰路由，区分集合资源、单个资源与动作型接口。

掌握：集合与单个资源路由；HTTP 方法表达操作；路径参数；固定路由优先于动态路由；嵌套资源与动作型接口。按学习安排跳过本趴练习。

### 第4章 第4趴：Path、Query、Header 与 Cookie

阶段：已学

目标：理解 FastAPI 如何根据函数签名识别不同请求参数来源，并使用类型注解与约束完成转换和校验。

掌握：Path、Query、Header、Cookie 参数来源；必填、可选和默认值；Header 别名；下划线到连字符转换；基本类型转换与 422 校验响应。

需要复习：`gt` 是严格大于，`ge` 是大于等于；`min_length` 约束字符数量。

### 第4章 第5趴：请求体与响应模型

阶段：已学

目标：使用 Pydantic Model 声明 JSON 请求体，理解请求校验、响应过滤、`response_model` 与 201 响应。

掌握：Pydantic Model 作为 JSON Body；字段约束与 422；请求模型和响应模型分离；`response_model` 校验、序列化并过滤输出；响应模型不匹配属于服务端错误。

### 第4章 第6趴：异常响应与统一错误结构

阶段：已学

目标：使用 `HTTPException` 表达可预期业务错误，区分业务异常与未知异常，并设计稳定的错误响应格式。

掌握：使用 `raise HTTPException` 表达业务错误；业务异常与未知异常分层；统一错误结构；通用 500 不泄露内部信息；详细 traceback 记录在服务端日志。

需要复习：HTTPException 的 detail 默认会出现在响应体的 `detail` 字段下；HTTP 状态码表达通用协议语义，业务错误码表达具体应用原因。

### 第4章 第7趴：OpenAPI 与 CRUD 小项目

阶段：已学

目标：把路由、参数、请求模型、响应模型、状态码和异常处理组合成可运行的内存 CRUD API，并通过 OpenAPI 文档验证接口契约。

当前掌握：请求/响应模型分离；response_model 建立输出边界；公共 404 查询函数；409 业务冲突与 422 参数校验的区别。

需要加强：PATCH 中未传字段与显式 null 的区别；204 必须没有响应体；内存存储的问题不是 I/O 高，而是无持久化、进程隔离和事务保障。

巩固状态：用户确认已掌握并跳过追加问答。

### 第5章 第1趴：BaseModel 与 DTO

阶段：已学

目标：理解 Pydantic 模型作为系统边界 DTO 的职责，掌握解析、校验、序列化、额外字段策略以及与领域/ORM 模型的区别。

当前掌握：默认类型转换；字符串清理；`extra="forbid"`；`model_dump()` 返回字典；Create/Update/Response 应分离。

需要加强：`ge` 包含边界值而 `gt` 不包含；DTO 按传输场景和职责区分，不是按不同用户区分。

巩固结果：已正确区分 `gt` 与 `ge`，并能解释 Update DTO 字段可选的原因。`internal_cost` 是企业内部成本等敏感业务字段，通常不应出现在公开 Response DTO。

### 第5章 第2趴：字段约束与默认值

阶段：已学

目标：掌握字符串、数值、集合约束，理解必填、默认值、`default_factory` 与可空字段的差异。

掌握：字符串/数值/集合约束；`gt/ge/lt/le`；必填、默认和可空；`default_factory`；`extra="forbid"`；类定义时默认值与实例创建时动态默认值。

注意：Pydantic 独立校验失败产生 `ValidationError`；FastAPI 在请求边界通常将其转换为 HTTP 422。

### 第5章 第3趴：字段与模型验证器

阶段：已学

目标：掌握 Pydantic v2 的 `field_validator` 与 `model_validator`，区分单字段规则、跨字段规则和验证前后的数据形态。

当前掌握：单字段转换使用 `field_validator`；跨字段关系使用 `model_validator`；I/O 和唯一性检查属于 Service/Repository；验证器必须返回转换后的值或模型自身。

需要加强：逐步追踪字符串转换链；验证器内部 ValueError 会被 Pydantic 汇总为 ValidationError，FastAPI 请求边界通常再转换为 422。

巩固状态：用户选择跳过追加练习，进入后续课程。

### 第5章 第4趴：嵌套模型与集合

阶段：已学

目标：使用嵌套 BaseModel、列表、字典和枚举描述复杂 JSON，并理解嵌套错误位置与共享模型复用。

掌握：嵌套 BaseModel 递归校验；列表元素转换为模型实例；Enum 限制取值；set 去重；tuple 固定结构；嵌套错误路径；避免滥用 Any。

需要复习：根据字段类型和 default_factory 判断默认容器，dict 对应 `{}`，set 对应 `set()`，list 对应 `[]`。

### 第5章 第5趴：序列化、反序列化与别名

阶段：已学

目标：掌握 `model_validate`、`model_dump`、JSON 序列化、字段别名以及输入别名与输出别名的边界。

当前掌握：model_validate 类型解析；model_dump 返回字典；exclude_none 过滤 None；Python 字段使用蛇形命名。

需要加强：alias_generator 会自动生成别名；populate_by_name 控制输入是否接受字段名；区分 JSON 兼容 Python 字典与已编码的 JSON 字符串。

### 第5章 第6趴：请求模型、响应模型与领域模型边界

阶段：已学

目标：区分 API 请求 DTO、响应 DTO、领域模型和 ORM 模型，理解数据在 HTTP、业务逻辑和数据库边界之间的转换。

本趴重点：请求模型只接收允许客户端提交的数据；响应模型只公开允许客户端看到的数据；领域模型承载业务规则；ORM 模型负责数据库映射；跨字段纯数据校验可放在 Pydantic，唯一性查询等 I/O 规则应放在 Service/Repository。

掌握：能够区分请求 DTO、响应 DTO 与 ORM 模型；理解 `from_attributes=True`；能说明响应模型对敏感字段的过滤作用。

需要加强：业务规则属于 Service；Repository 负责执行查询和持久化，不负责决定业务规则。

### 第5章 第7趴：Pydantic v2 高频面试题

阶段：已学，后续随机回测

目标：整合 BaseModel、字段约束、验证器、序列化、别名和模型边界，并使用准确术语回答常见追问。

### 第6章 第1趴：WSGI、ASGI 与 Uvicorn

阶段：已学

目标：理解 Web Server、网关接口与 Web 框架的职责边界；掌握 WSGI 和 ASGI 的核心区别，以及 Uvicorn 启动 FastAPI 应用时发生的事情。

掌握：能够区分 FastAPI、Uvicorn 和 ASGI；能够还原请求从网络进入路由再返回客户端的主链路；理解 ASGI 不会自动消除同步阻塞。

需要加强：替换 `time.sleep()` 时要根据真实任务选择异步 API、线程、进程或任务队列；Repository 应描述为数据访问层，不是业务校验层。

### 第6章 第2趴：FastAPI 请求生命周期

阶段：已学

目标：理解一次请求从 Uvicorn 进入 FastAPI 后，依次经过 Middleware、路由匹配、依赖解析、参数校验、路由函数、响应模型与异常处理的过程。

掌握：能够说明成功请求与请求校验失败的执行路径；理解校验失败不会执行路由函数；能够区分返回错误字典和抛出 `HTTPException`；大部分横切职责与分层职责判断正确。

需要加强：跨多个数据操作的完整业务流程属于 Service；参数校验的意义不仅是避免报错，还包括在系统边界阻止无效数据和副作用进入业务层。

### 第6章 第3趴：依赖注入与 `Depends`

阶段：已学

目标：理解依赖注入解决的问题、FastAPI 如何从函数签名构建依赖树，以及依赖缓存、子依赖和常见使用场景。

掌握：能够区分函数对象与调用结果；能够还原子依赖执行顺序；理解依赖失败会阻止后续依赖和路由执行；掌握单次请求缓存及 `use_cache=False`。

需要加强：数据库 Session 等可注入且需要清理的路由资源适合 Dependency，而不是 Middleware；依赖在路由函数之前完成解析，不应表述为“执行路由函数时才调用”。

### 第6章 第4趴：`yield` 依赖与资源清理

阶段：已学

目标：理解 `yield` 前后的进入与退出语义，掌握数据库 Session 等资源的创建、注入、异常传播与可靠清理。

掌握：理解 `yield` 前创建、路由中使用、`finally` 中清理；能够判断异常不会被 `finally` 自动吞掉；掌握多层依赖按创建顺序的反方向清理。

需要加强：Python 使用 `try/finally` 而不是 JavaScript 花括号语法；`rollback` 属于事务管理；同步阻塞 I/O 转线程的准确 API 是 `asyncio.to_thread()`。

### 第6章 第5趴：Middleware

阶段：已学

目标：掌握 Middleware 的洋葱模型、多个 Middleware 的执行顺序、适用边界，以及它与 Dependency、Exception Handler 的区别。

掌握：能够准确判断多个 Middleware 的请求和响应顺序；理解异常时 `response` 可能尚未赋值；能够区分 Middleware、Dependency 和 Exception Handler；具备请求日志的安全意识。

需要加强：描述 `yield` 时使用“在 `yield` 处暂停，之后恢复执行”，避免使用“`yield` 中断后再次执行”等容易产生歧义的表达。

### 第6章 第6趴：Lifespan 与应用启动/关闭

阶段：已学

目标：区分应用级生命周期与请求级生命周期，掌握启动时初始化共享资源、关闭时释放资源，以及多 Worker 下资源并不跨进程共享。

掌握：能够区分 Lifespan 与 `yield` Dependency 的资源范围；理解每个 Worker 独立执行 Lifespan 并持有独立内存；能够识别模型重复加载和调度任务重复执行问题。

需要加强：跨 Worker 限流通常依赖 Redis 原子操作或专门限流服务；独立 Worker 主要解决调度或后台任务的唯一执行，不直接代替共享限流状态。

### 第6章 第7趴：同步路由、异步路由与线程池

阶段：已学

目标：理解 FastAPI 如何执行 `async def` 与普通 `def` 路由，掌握事件循环、线程池、同步阻塞 I/O 与 CPU 密集任务的正确选型。

掌握：能够判断异步客户端、同步 SDK、混合 I/O 和 CPU 密集任务的执行方案；理解普通辅助函数不会自动进入线程池；能够分析线程池饱和风险。

需要加强：完整写法是 `await asyncio.to_thread(function, *args)`；`app.state` 只在当前应用进程内共享，不能跨 Worker 称为全局共享。

### 第6章 第8趴：FastAPI 原理面试追问与章节收束

阶段：已学，后续随机回测

目标：整理第 6 章核心面试表达，通过后续章节随机回测 ASGI、请求生命周期、依赖注入、Middleware、Lifespan 和线程池调度。

章节评价：能够解释 Uvicorn、ASGI 与 FastAPI 的边界，还原请求生命周期，区分 Middleware、Dependency、Exception Handler 和 Lifespan，并为同步/异步 I/O 选择执行方式。主要复习点是资源与事务职责、进程级共享边界，以及 `await asyncio.to_thread(function, *args)` 的准确写法。

### 第7章 第1趴：关系模型、表与约束

阶段：已学

目标：理解关系数据库中的表、行、列、主键和外键，掌握 `NOT NULL`、`UNIQUE`、`PRIMARY KEY`、`FOREIGN KEY`、`CHECK` 与 `DEFAULT` 的职责，并理解应用校验不能替代数据库约束。

掌握：理解主键、外键和引用完整性；能够为必填、唯一、非负值和状态范围选择基本约束；理解多 Worker 下数据库唯一约束是最终防线。

需要加强：IDENTITY 的完整语法；类型必须写在约束之前；普通 `UNIQUE` 默认允许多个 NULL；`CHECK` 的 UNKNOWN 不会拒绝 NULL；唯一冲突使用 `try/except + rollback`，不是 `try/finally`。

### 第7章 第2趴：SQL 查询、聚合与子查询

阶段：已学

目标：掌握 `SELECT`、`WHERE`、`ORDER BY`、`LIMIT`、聚合函数、`GROUP BY`、`HAVING` 与基础子查询，并理解 SQL 的逻辑处理顺序。

掌握：理解 `WHERE` 不能过滤聚合结果；掌握 `COUNT(*)` 与 `COUNT(column)` 的 NULL 差异；能够编写标量子查询；能够解释 CHECK 遇到 NULL 的 UNKNOWN 语义。

需要加强：`ASC`/`DESC` 方向；SELECT 字段之间的逗号；聚合时补全 `GROUP BY`；排序使用聚合表达式或别名；空集上的 `SUM` 返回 NULL 而不是报错。

### 第7章 第3趴：JOIN

阶段：已学

目标：掌握 `INNER JOIN`、`LEFT JOIN`、自连接与多表连接，理解连接条件、过滤位置、重复行和一对多关系对结果集的影响。

掌握：理解 INNER JOIN 与 LEFT JOIN 的语义；能够解释 ON 与 WHERE 对外连接的不同影响；理解一对多导致结果行扩张。

需要加强：严格使用真实表名和列名；多表共有字段必须带表别名；统计所有左表记录时使用 LEFT JOIN；右表筛选放在 ON；聚合查询补全 GROUP BY；复习 COALESCE。

### 第7章 第4趴：索引与执行计划

阶段：已学

目标：理解索引的数据结构与代价，掌握单列/复合索引、最左前缀、选择性、覆盖索引基础，以及使用 `EXPLAIN`/`EXPLAIN ANALYZE` 阅读执行计划。

掌握：理解索引是额外查找结构及其读写权衡；能够判断选择性与 Seq Scan 的合理性；掌握复合索引的前导列思维；能够区分表达式、部分和覆盖索引；理解常见扫描节点、估算与实际行数、loops 和 `EXPLAIN ANALYZE` 的执行风险。

学习方式反馈：采用四个小回合的图示、类比和选择题后，基础与综合判断全部正确。后续数据库课程继续采用“概念画面 → 选择判断 → 半成品纠错 → 必要时再写 SQL”的阶梯方式。

### 第7章 第5趴：事务与隔离级别

阶段：已学

目标：理解事务的原子性、一致性、隔离性和持久性，掌握提交与回滚，并通过并发场景理解脏读、不可重复读、幻读以及 PostgreSQL 隔离级别。

掌握：能够用业务场景解释 ACID；准确区分脏读、不可重复读、幻读和丢失更新；理解 Read Committed、Repeatable Read 与 Serializable 的快照差异；能够说明 Service 事务边界、失败回滚、整事务重试和外部副作用幂等。

需要加强：Read Committed 的变化发生在不同语句快照之间；普通查询与稳定报告的隔离级别选择；`asyncio.to_thread()` 接收同步阻塞函数对象。

### 第7章 第6趴：MVCC

阶段：已学

目标：理解 PostgreSQL 为什么更新行时会产生新版本、不同事务如何根据快照看到不同版本，以及长事务、死元组、VACUUM 与表膨胀之间的关系。

第 1 小回合掌握：理解 UPDATE 需要保留旧行版本，以满足仍持有旧快照的事务；未提交的新版本对其他普通事务不可见；知道 MVCC 能降低读写阻塞，但不会消除写写冲突和锁；能够说明多版本会带来清理、存储与表膨胀成本。

表达修正：不是“MVCC 创建多个版本的快照”，而是数据更新会产生多个行版本，事务取得快照后依据可见性规则选择自己能看到的行版本。

第 2 小回合掌握：能够准确推演 Read Committed 与 Repeatable Read 下的版本可见性；理解其他事务未提交的数据不可见，而事务自己的未提交修改可见；能够用装饰器嵌套结构 `A(B(work))` 解释多层装饰器的装饰顺序和调用顺序。

表达修正：PostgreSQL 的 Repeatable Read 快照通常在事务中第一条非事务控制语句开始时建立，并非执行 `BEGIN` 的瞬间建立。

第 3 小回合掌握：理解 UPDATE/DELETE 淘汰的旧行版本会形成死元组；能够区分普通 `VACUUM` 的空间复用与 `VACUUM FULL` 的表重写和磁盘空间归还；知道 autovacuum 长期关闭会造成死元组堆积、表膨胀和性能下降；浅拷贝回测结论正确。

表达修正：普通 `VACUUM` 通常使死元组占用的空间可供数据库再次使用，不等于表文件立刻缩小；浅拷贝后的两个字典起初也可能引用同一个不可变字符串，给 `cloned["name"]` 重新赋值属于重新绑定，并不是因为字符串被“复制了一份”。

第 4 小回合掌握：理解长事务持有旧快照会拖住旧版本清理，并可能导致死元组堆积、表膨胀、连接与锁长期占用；能够正确使用 `asyncio.to_thread(sync_function)` 转移同步阻塞 I/O。

需要加强：遇到“死元组持续升高且 autovacuum 最近运行”的场景时，使用 `pg_stat_activity` 检查长事务和 `idle in transaction`；必要时结合 `pg_locks` 检查锁等待。

### 第7章 第7趴：锁、死锁与并发更新

阶段：已学

目标：区分普通读取、行级锁和表级锁；理解并发更新为什么等待、死锁如何形成，以及如何通过固定加锁顺序、缩短事务和整事务重试降低风险。

第 1 小回合掌握：理解普通 `SELECT` 通常不受行锁阻塞，修改或 `FOR UPDATE` 锁定同一行需要等待；知道行锁通常保持到事务提交或回滚；能够正确匹配 FastAPI 的 422、404、409、504 状态码。

需要加强：行锁只影响发生冲突的同一行，不会让其他行的写操作等待。

第 2 小回合掌握：能推演两个扣款请求通过 `SELECT ... FOR UPDATE` 依次读取最新余额的过程；理解锁内应只保留读取、校验和更新等必要数据库操作；知道数据库内的 `balance = balance - :amount` 可避免应用层先读后算再覆盖导致的丢失更新。

需要加强：`lifespan` 除数据库 Engine/连接池外，也适合共享 HTTP 客户端、模型等应用级长生命周期资源；每次请求独立的数据库 Session 仍应使用依赖注入创建和清理。

第 3 小回合掌握：能够识别循环等待导致的死锁，理解数据库会中止其中一个事务，应用应回滚后重试整个事务；能够解释可变默认参数的共享原因与 `None` 哨兵修复方案。

需要加强：多行加锁的统一顺序应从真实输入 `from_id`、`to_id` 计算；固定顺序用于预防死锁，而长时间外部调用会增加死锁风险。

第 4 小回合掌握：理解乐观锁通过 `id + version` 条件让过期写入更新 0 行，知道用户偶发编辑冲突适合优先考虑乐观锁；能够判断无限重试不合理。

需要加强：并发冲突后不能默认自动重做用户原意；简单余额扣减优先考虑数据库原子条件更新，复杂多行校验场景再选择悲观锁；复习 `await` 与 `asyncio.create_task()` 的调度时机。

### 第7章 第8趴：分页与慢查询优化

阶段：已学

目标：理解 OFFSET 分页的稳定排序和深分页代价，掌握游标分页的基本思想，以及从慢查询现象走向索引、SQL 与执行计划排查的路径。

第 1 小节掌握：能够说明 OFFSET 分页必须使用确定且唯一的排序（如 `created_at DESC, id DESC`）；能够根据页码计算 OFFSET，并解释大 OFFSET 会处理大量最终被丢弃的记录；上下文管理器异常清理回测正确。

第 2 小节掌握：能够正确选择 OFFSET 与游标分页的典型适用场景；理解游标由排序字段与唯一字段共同组成，倒序分页使用“小于上一页游标”的条件；能区分重新绑定与原地修改。

第 3 小节掌握：知道慢接口先定位耗时点，再获取真实 SQL 与参数；能够区分 `EXPLAIN` 的计划预测与会实际执行 SQL 的 `EXPLAIN ANALYZE`，并识别后者对写操作有副作用；Pydantic 三种排除规则回测正确。

需要加强：看到 `Seq Scan`、大量 `Rows Removed by Filter` 且返回很少行时，进一步检查查询条件/排序与索引是否匹配，并核查统计信息是否失真；`exclude_unset=True` 指排除“调用模型时未显式提供”的字段，不是泛指未定义字段。

第 4 小节掌握：能够按数据量与选择性判断 Seq Scan、Index Scan、Bitmap Heap Scan 的合理性，不再把 Seq Scan 机械等同于性能问题；能够正确写出 `await asyncio.to_thread(slow_sync_request)`。

第 5 小节状态：已讲解，练习按当前学习安排跳过；保留 `Index Cond`、`Filter`、`Sort` 与“估算/实际行数差异”的内容，后续在 SQLAlchemy 的真实查询中回测。

### 第8章 第1趴：ORM、Model 与映射

阶段：学习中

目标：理解 ORM 解决的边界问题，能区分 ORM Model、Pydantic DTO 和数据库表，并掌握 SQLAlchemy 2.x 声明式模型的基础结构。

第 1 小节掌握：理解 ORM Model、请求 DTO、响应 DTO 的职责不同；能解释 `__tablename__`、`Mapped[T]`、`mapped_column()` 的映射含义；能从安全与职责分离解释为何 Create 与 Response DTO 必须分开。

需要加强：`password` 只属于创建/改密请求 DTO，`password_hash` 只属于 ORM/数据库层，`id` 通常由数据库生成并出现在 ORM/响应 DTO；避免把请求字段直接照搬到 ORM。

### 第9章 第1趴：Redis 数据结构与缓存基础

阶段：学习中

目标：理解 Redis 的内存键值模型、常用数据结构和过期时间，能判断哪些数据适合缓存，以及缓存与数据库各自承担什么职责。

学习方式：使用 [`09-redis/docker-compose.yml`](./09-redis/docker-compose.yml) 启动独立 Redis 实例；先在 `redis-cli` 中观察命令结果，再逐步接入 FastAPI。

目录映射：本趴包含实验 1（String/TTL）、实验 2（Hash 局部更新）、实验 3（List/Set/Sorted Set）和一个 FastAPI 读写 Key 小实践；完成它们才进入第 2 趴缓存策略。后续每一趴同样在目录中列出实验与工程实践，不再让“实验编号”脱离课程目录。

实验 1 完成：已通过 `SET`、`GET`、`EX`、`TTL` 观察 String 与键过期；能正确判断 `TTL=10` 表示剩余时间、过期后 `GET` 返回 `nil`、`TTL=-2` 表示键不存在。

实验 2 完成：理解 Hash 的字段结构和局部更新；知道更新 `city` 不会影响同一 Hash 中的 `name`、`level`，且 `EXPIRE user:1001 60` 设置的是整个 Key 的 TTL。实验 Key 在复核时已正常过期，进一步印证 TTL 作用于整个 Key。

实验 3 完成：能通过 CLI 验证 List 的 FIFO 行为、Set 的去重与成员计数、Sorted Set 的 score 排序和增量更新；能够依据任务队列、点赞集合、积分排行榜的业务操作需求选择对应数据结构。

小实践完成：已用 FastAPI 在 `lifespan` 中创建共享异步 Redis 客户端，实现带 TTL 的 Key 写入、读取和缓存未命中 404；理解客户端不应逐请求创建。

第 1 趴回顾：已掌握 String、Hash、List、Set、Sorted Set 的典型选择，能解释 TTL 到期后 Key 不存在，能经由 FastAPI 读写带 TTL 的缓存。需要注意：对指定 Key 进行覆盖式写入选择 `PUT`，其关键 REST 语义是幂等；“设置缓存”本身不是完整理由。

### 第9章 第2趴：缓存与过期策略

阶段：学习中

目标：掌握缓存 Key 设计、TTL 选择、主动失效与被动过期的边界，理解缓存命中/未命中、陈旧数据和内存风险之间的权衡。

实验 4 完成：能通过 CLI 验证 String Key 被不带 TTL 的 `SET` 覆盖后 `TTL=-1`，理解这是“Key 存在但永不过期”；知道 `KEEPTTL` 在覆盖值时保留剩余 TTL；能够为验证码重发选择重新设置 TTL，为固定时间窗口内更新的数据选择保留 TTL。

历史回测：能正确推演 `model_dump(exclude_unset=True)`：未传字段会被排除，显式传入 `null` 的字段会保留为 `None`；理解 PATCH 用它避免未提供字段被默认值意外覆盖。

实验 5 进展：理解详情与库存更新频率不同，库存可使用更短 TTL；需要加强缓存 Key 的职责分隔（独立 TTL / 独立失效）以及统一命名顺序，例如 `cache:user:1001:profile:v1`。

实验 6 完成：能正确判断 `DEL` 后 `GET=nil`、`TTL=-2`；理解数据源写入成功后应尽快主动删除旧缓存，TTL 只限制最长陈旧时间；能区分验证码自然失效主要依赖 TTL、商品价格变更主要依赖主动 DEL。

第 2 趴回顾：已掌握 Key 的命名层次、TTL 覆盖陷阱、`KEEPTTL`、版本隔离与写数据库后主动删除缓存；能结合验证码、商品详情和库存选择不同失效方式。需要加强：Key 设计题只写 Key，不混入命令和 Value；Key 拆分的直接工程收益是独立 TTL 和独立失效。

历史回测：能识别两个事务反向锁定两行导致的死锁，知道固定升序加锁顺序可预防。表达补充：死锁受害事务被数据库回滚后，先前读取、校验和写入上下文均可能失效，因此必须从头重试整个事务，不能只重试最后一条 SQL。

### 第9章 第3趴：Cache Aside

阶段：已学

目标：用 FastAPI 实现缓存旁路读写链路：读时 Cache → DB → 回填 Cache，写时先更新 DB 再删除 Cache；理解缓存不是数据真相来源。

实验 7 完成：已在 FastAPI 中观察 Cache Aside：首次读取 miss 并回填 Redis，后续读取 hit；更新模拟数据库成功后删除缓存，下一次读取重新从数据源获取最新值并回填。能够解释写失败时不应提前删除缓存，以及不删除缓存会导致读到旧值。

第 3 趴回顾：已掌握 Cache Aside 的读路径 `Cache → 数据源 → 回填 Cache` 和写路径 `写数据源成功 → DEL Cache`；能解释缓存命中/未命中、旧缓存导致的陈旧读，以及缓存作为可重建副本而非真相来源。

历史回测：能够推演 `asyncio.create_task()` 的并发执行：A、B 可在 `await` 处交替推进，整体耗时接近较长任务；即使 B 先完成，`await task_a`、`await task_b` 的变量赋值和最终打印顺序仍由代码位置决定。

### 第9章 第4趴：缓存穿透、击穿与雪崩

阶段：学习中

目标：区分不存在数据反复查询导致的缓存穿透、热点 Key 重建并发导致的缓存击穿、大量 Key 同时失效导致的缓存雪崩，并为每种问题选择不同防护手段。

实验 8 完成：通过 FastAPI 重复请求不存在商品并观察数据源读取计数，理解不存在记录不会自然回填正常缓存，导致每次请求穿透到数据源；能够提出空值缓存（短 TTL sentinel）作为基础防护。

实验 9 完成：已接入并验证空值缓存：同一不存在商品的多个请求仍返回 404，但只首次访问数据源，后续命中短 TTL `__NOT_FOUND__` sentinel；能说明空值不能永久缓存，并在数据创建时主动删除空值缓存、由下次读取回填真实数据。

实验 10 完成：使用并发请求验证热点真实商品缓存失效后会发生多次并发回源；能够区分缓存击穿与缓存穿透，并提出互斥锁/单飞机制让一个请求重建、其他请求等待或稍后读取缓存的防护方向。

实验 11 完成：理解统一 TTL 会让大量 Key 在相近时刻失效并造成缓存雪崩，能说明 TTL 抖动通过分散失效时间降低集中回源；能区分它不能解决单热点击穿，也不能解决 Redis 整体不可用。

历史回测：能正确区分 Middleware（全局请求日志）、yield Dependency（每请求 Session 生命周期）、Exception Handler（异常转统一响应）和普通 Dependency（解析当前用户）。

实验 12 完成：通过 Python 模拟布隆过滤器，能够说明 `False` 代表一定不存在、`True` 仅代表可能存在，理解假阳性只会多一次后续查询；知道新建数据后必须将 ID 加入过滤器，否则可能被错误拦截。

实验 13 完成：通过异步小实验观察逻辑过期：过期缓存可先返回旧值，单个后台任务刷新后后续请求读到新值。能够区分它与“等待重建”的互斥锁方案，并能判断详情页可接受短暂陈旧数据，而库存校验不可接受。

实验 14 完成：理解 Redis 整体故障会使流量集中回源并压垮数据库；知道高可用用于降低缓存层整体故障概率，限流用于限制接口/租户/IP 或下游回源速率，降级可返回旧副本、简化内容或“稍后重试”。需要加强：多实例下 `asyncio.Lock()` 不共享，应使用带唯一 token 与超时的 Redis 分布式锁（第 5 趴实操）。

第 4 趴回顾：已能区分并匹配主要缓存风险：不存在请求使用空值缓存与布隆过滤器；热点 Key 失效使用互斥重建/单飞或逻辑过期；大量 Key 集中失效采用 TTL 抖动；缓存层整体故障依赖高可用，并由限流与降级保护数据源。注意：不同方案解决的故障范围不同，不能拿 TTL 抖动解决 Redis 宕机，也不能用逻辑过期处理库存等强一致性判断。

历史回测：能识别先读后算再覆盖写入造成的丢失更新；需要加强简单扣款的数据库原子条件更新，以及“并发不等于必须加悲观锁”的选型边界。

历史回测：能说明 DTO 适合无 I/O 的价格范围校验，Pydantic 验证器不适合数据库同名查询；需要记住字段约束写法为 `Field(gt=0)`，并补充数据库 UNIQUE 才是同名约束的最终防线。

历史回测：能够准确解释可变默认参数在函数定义时创建并被后续调用共享，能使用 `None` 哨兵值在函数内部创建新列表。

## 学习日志

### 第1章 第1趴

阶段：已学

掌握： - 🟩 对象引用 - 🟩 可变对象 - 🟩 不可变对象 - 🟩 == / is - 🟩
None 判断

需要复习： - Rebinding - Reference - 官方术语表达

下一趴： 为什么 Python 默认参数不能使用 \[\] 或 {}？

### 第1章 第2趴

阶段：已学

掌握：可变默认参数、定义时求值、`None` 哨兵值、显式传入可变对象时的共享、复制后再修改。

需要复习：严格判断 print 的表达式及其执行时刻；使用“对象引用”代替“地址”。

下一趴：浅拷贝与嵌套可变对象。

### 第1章 第3趴

阶段：已学

掌握：浅拷贝、深拷贝、嵌套可变对象共享、重新绑定与原地修改的区别。

需要复习：浅拷贝复制元素引用；用“对象引用”代替“引用地址”。

下一趴：函数参数传递。

### 第1章 第4趴

阶段：已学

掌握：对象共享传递、局部形参重新绑定、通过形参原地修改实参可变对象。

需要复习：描述对象关系时使用“引用同一个对象”，避免使用“同一个地址”。

下一趴：参数类型与 `*args`、`**kwargs`。

### 第1章 第5趴

阶段：已学

掌握：位置参数、关键字参数、默认参数、定义时收集、调用时展开、空元组与空字典。

需要复习：Python 布尔值使用 `True/False`；`**mapping` 的键成为参数名。

下一趴：仅位置参数与仅关键字参数。

### 第1章 第6趴

阶段：已学

掌握：仅位置参数、仅关键字参数、`/` 与 `*` 的签名边界。

需要复习：题目要求判断成功时，还要写出使用默认值后的完整输出。

下一趴：作用域与 LEGB。

### 第1章 第7趴

阶段：已学

掌握：LEGB、局部名称判定、`UnboundLocalError`、`global`、`nonlocal`。

下一趴：一等函数与闭包。

### 第1章 第8趴

阶段：已学

掌握：一等函数、返回函数对象、闭包、独立闭包状态、`nonlocal` 更新状态。

需要复习：读取外层名称不要求 `nonlocal`；只有需要对外层名称重新绑定时才需要。

下一章：Python 进阶——装饰器。
