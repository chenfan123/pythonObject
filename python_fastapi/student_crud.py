from os import name
from models import Student
from settings import TEST_ORM
from tortoise import Tortoise
import asyncio
from typing import List
# 创建学生函数


async def create_student(name: str, age: int, email: str = None) -> Student:
    try:
        student = await Student.create(name=name, age=age, email=email)
        return student
    except Exception as e:
        print(f"Error creating student: {e}")


async def update_student(stu_id: int, name: str = None, age: int = None, email: str = None) -> Student:
    try:
        student = await Student.get(id=stu_id)
        # 判断用户传递了哪个数据，没传就不更新
        if name:
            student.name = name
        if age is not None:
            student.age = age
        if email is not None:
            student.email = email
        # 保存修改
        await student.save()
        # 返回修改后的学生对象
        return student
    except Exception as e:
        print(f"Error updating student: {e}")


async def delete_student(stu_id: int) -> bool:
    try:
        student = await Student.get(id=stu_id)
        await student.delete()
        return True
    except Exception as e:
        print(f"Error deleting student: {e}")
        return False

# 查询
# 单条数据


async def get_student(stu_id: int) -> Student:
    try:
        student = await Student.get(id=stu_id)
        return student
    except Exception as e:
        print(f"Error getting student: {e}")
        return None

# 多条数据


async def get_students() -> List[Student]:
    try:
        # students = await Student.all() # 获取所有数据
        # students = await Student.filter(age__gt=20) # 完全匹配
        students = await Student.filter(name__contains=name)  # 模糊匹配
        return students
    except Exception as e:
        print(f"Error getting students: {e}")
        return []
# 1. 直接测试脚本

# 初始化数据库


async def init():
    await Tortoise.init(config=TEST_ORM)
    await Tortoise.generate_schemas()

# 主函数


async def main():
    await init()
    # stu1 = await create_student("John Doe", 20, "john.doe@example.com")
    # stu2 = await create_student("Jane Doe", 21, "jane.doe@example.com")
    # stu3 = await create_student("Jim Doe", 22, "jim.doe@example.com")
    # stu4 = await create_student("Jim Doe2", 22, "jim.doe2@example.com")
    await update_student(1, name="John Doe1111", age=31, email="john.doe1111@example.com")
    await delete_student(2)
    await Tortoise.close_connections()

# 2. 直接应用到接口


if __name__ == "__main__":
    asyncio.run(main())
