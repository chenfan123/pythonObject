# 关联关系建立 1对1
# 模型定义见 relation_models.py（文件名可被 Tortoise 导入）
from relation_models import Student, StudentProfile
from settings import RELATION_ORM
from tortoise import Tortoise
import asyncio
from rich import print

"""
示例数据示意：

Student
id  name
1   张三
2   李四

StudentProfile
id  address  phone
1   上海     123456
2   北京     789456

本文件 OneToOneField 在 Student 上 → students.profile_id 指向 student_profiles.id
"""


async def init_db():
    await Tortoise.init(config=RELATION_ORM)
    await Tortoise.generate_schemas()
    print("relation_db 表已创建: students, student_profiles")


async def main():
    await init_db()
    # 演示：先建资料，再绑到学生
    p1 = await StudentProfile.create(address="上海", phone="123456")
    p2 = await StudentProfile.create(address="北京", phone="789456")
    s1 = await Student.create(name="张三", profile=p2)
    s2 = await Student.create(name="李四", profile=p1)
    # Tortoise 默认 print(model) 只显示 <Student>，要看字段用 __str__ 或手动拼
    print(f"{s1} -> {await s1.profile}")
    print(f"{s2} -> {await s2.profile}")
    print(f"反向: {(await p1.student).name} 的资料是 {p1.address}")
    print(f"反向: {(await p2.student).name} 的资料是 {p2.address}")
    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
