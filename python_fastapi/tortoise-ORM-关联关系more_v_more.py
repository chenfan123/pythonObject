# 关联关系建立 多对多（显式中间表 CourseStudent）
from relation_models_more_v_more import Student, StudentProfile, Course, CourseStudent, Grade
from settings import RELATION_ORM_MORE_V_MORE
from tortoise import Tortoise
import asyncio
from rich import print

"""
Student <-> Course 多对多，中间表 course_students

Student          Course
1 张三           1 数学
2 李四           2 英语

CourseStudent
id  course_id  student_id
1   1          1   # 张三-数学
2   2          1   # 张三-英语
3   1          2   # 李四-数学
"""


async def init_db():
    await Tortoise.init(config=RELATION_ORM_MORE_V_MORE)
    await Tortoise.generate_schemas()
    print(
        "relation_db_more_v_more 表已创建: "
        "students, student_profiles, grades, courses, course_students"
    )


async def create_data():
    await init_db()
    # 1对1
    st1 = await Student.create(name="张三")
    pro1 = await StudentProfile.create(address="上海", phone="123456")
    st1.profile = pro1
    await st1.save()
    pro2 = await StudentProfile.create(address="北京", phone="789456")
    stu2 = await Student.create(name="李四", profile=pro2)

    # 1对多
    stu3 = await Student.create(name="王五")
    grade1 = await Grade.create(score=90, student=stu3)
    grade2 = await Grade.create(score=80, student=stu3)
    grade3 = await Grade.create(score=70, student=stu3)

    # 多对多
    stu4 = await Student.create(name="赵六")
    stu5 = await Student.create(name="孙七")
    cou2 = await Course.create(name="数学")
    cou3 = await Course.create(name="英语")
    cs1 = await CourseStudent.create(course=cou2, student=stu4)
    cs2 = await CourseStudent.create(course=cou2, student=stu5)
    cs3 = await CourseStudent.create(course=cou3, student=stu4)
    cs4 = await CourseStudent.create(course=cou3, student=stu5)

    await Tortoise.close_connections()


async def update_data():
    await init_db()
    # 1对1
    st1 = await Student.get(id=1)
    pro1 = await StudentProfile.get(id=1)
    st1.profile = pro1
    await st1.save()

    # 1对多
    stu2 = await Student.get(id=2)
    grade1 = await Grade.get(id=1)
    grade1.student = stu2
    await grade1.save()
    # 1对多
    await Grade.filter(id=6).update(student=stu2)

    # 多对多 类似


async def query_data():
    await init_db()
    # ¥
    stu = await Student.get(id=1)
    print(f"学生: {stu.name}")
    pro = await stu.profile  # 关联查询
    print(f"学生档案: {pro.address} {pro.phone}")

    # 预加载关联数据,表示要获取关联数据
    stu2 = await Student.get(id=2).prefetch_related("profile")
    print(f"学生: {stu2.name}")
    print(f"学生档案: {stu2.profile.address} {stu2.profile.phone}")

    # 1对多
    stu3 = await Student.get(id=3).prefetch_related("grades")
    for grade in stu3.grades:
        print(f"学生: {stu3.name} 成绩: {grade.score}")

    # 多对多
    stu4 = await Student.get(id=4).prefetch_related("courses")
    for course in stu4.courses:
        print(f"学生: {stu4.name} 选修课程: {course.name}")


async def delete_data():
    await init_db()
    # 1对1
    st1 = await Student.get(id=1)
    await st1.delete()

if __name__ == "__main__":
    asyncio.run(create_data())
