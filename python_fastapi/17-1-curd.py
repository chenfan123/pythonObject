from models import Student
from settings import TEST_ORM
from tortoise import Tortoise
import asyncio

# 创建学生函数


async def create_student(name: str, age: int, email: str = None) -> Student:
    try:
        student = await Student.create(name=name, age=age, email=email)
        return student
    except Exception as e:
        print(f"Error creating student: {e}")

# 1. 直接测试脚本

# 初始化数据库


async def init():
    await Tortoise.init(
        db_url="postgres://learn:learn@127.0.0.1:5433/test_db",
        modules={"models": ["models"]},
    )
    await Tortoise.generate_schemas()

# 主函数


async def main():
    await init()
    stu1 = await create_student("John Doe", 20, "john.doe@example.com")
    stu2 = await create_student("Jane Doe", 21, "jane.doe@example.com")
    stu3 = await create_student("Jim Doe", 22, "jim.doe@example.com")
    stu4 = await create_student("Jim Doe2", 22, "jim.doe2@example.com")
    await Tortoise.close_connections()

# 2. 直接应用到借口


if __name__ == "__main__":
    asyncio.run(main())
