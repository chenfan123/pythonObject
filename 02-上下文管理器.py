# 用于管理具有明确“进入”和“退出”阶段的资源
# 文件；数据库连接；数据库事务；锁；网络连接；临时目录。
# 常见写法
# 即使读取过程中发生异常，退出 with 时也会尝试关闭文件。
# 核心价值：无论代码正常结束还是发生异常，都执行资源清理。
with open("data.txt", "r") as file:
    content = file.read()

# 自定义上下文管理


class DatabaseConnection:
    def __enter__(self):
        print("连接数据库")
        return self

    def query(self):
        print("执行查询")

    def __exit__(self, exc_type, exc_value, traceback):
        print("关闭数据库连接")
        return False


with DatabaseConnection() as database:
    database.query()
# 创建 DatabaseConnection 对象 → 调用 __enter__() → 将 __enter__() 的返回值赋给 database → 执行 with 代码块 → 调用 __exit__()
# return self 决定了 as 后面得到什么

# __exit__() 的三个异常参数
# exc_type：异常类型；
# exc_value：异常对象；
# traceback：调用栈信息。

# __exit__() 的返回值
# return False： 表示不吞掉异常，异常继续向外传播。
# return True：表示异常已经处理，不再向外传播。
# 默认返回 None，效果与 False 相同：异常继续传播。
