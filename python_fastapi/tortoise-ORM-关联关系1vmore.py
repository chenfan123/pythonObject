# 关联关系建立 1对多
# 模型定义见 relation_models1vmore.py
from relation_models1vmore import Student, StudentProfile, Grade
from settings import RELATION_ORM_1VMORE
from tortoise import Tortoise
import asyncio
from rich import print

"""
示例：一个学生多条成绩（外键在 Grade.student）

Student
id  name
1   张三
2   李四

Grade
id  score  student_id
1   90     1
2   85     1
3   78     2
"""


async def init_db():
    await Tortoise.init(config=RELATION_ORM_1VMORE)
    await Tortoise.generate_schemas()
    print("relation_db_1vmore 表已创建: students, student_profiles, grades")


async def main():
    await init_db()

    p1 = await StudentProfile.create(address="上海", phone="123456")
    p2 = await StudentProfile.create(address="北京", phone="789456")
    s1 = await Student.create(name="张三", profile=p2)
    s2 = await Student.create(name="李四", profile=p1)

    g1 = await Grade.create(score=90, student=s1)
    g2 = await Grade.create(score=85, student=s1)
    g3 = await Grade.create(score=78, student=s2)

    s1_grades = await s1.grades.all()
    s2_grades = await s2.grades.all()
    print(f"{s1} 的成绩: {[str(g) for g in s1_grades]}")
    print(f"{s2} 的成绩: {[str(g) for g in s2_grades]}")
    print(f"{g1} 属于 {(await g1.student).name}")
    print(f"{g3} 属于 {(await g3.student).name}")
    print(f"共创建成绩 {g1.id}, {g2.id}, {g3.id}")

    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
