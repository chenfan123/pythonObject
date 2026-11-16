# 关联关系模型（1对多），供 Tortoise / aerich 导入
# 1对多关系建立在多的那边，在多的那边建立外键
from tortoise import fields, models


class Student(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    # OneToOne 声明在 Student 侧 → students 表会有 profile_id
    profile = fields.OneToOneField(
        "models.StudentProfile",
        on_delete=fields.CASCADE,  # 级联删除
        related_name="student",  # 关联名称
        null=True,  # 允许为空
    )

    class Meta:
        table = "students"

    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"


class StudentProfile(models.Model):
    id = fields.IntField(pk=True)
    address = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=20)

    class Meta:
        table = "student_profiles"

    def __str__(self):
        return f"StudentProfile(id={self.id}, address={self.address}, phone={self.phone})"


#
class Grade(models.Model):
    id = fields.IntField(pk=True)
    score = fields.FloatField()
    student = fields.ForeignKeyField(
        "models.Student",
        on_delete=fields.CASCADE,  # 级联删除
        related_name="grades"  # 关联名称，在 Student 模型中可以通过 student.grades 访问所有成绩
    )  # 外键指向 Student 模型

    class Meta:
        table = "grades"

    def __str__(self):
        return f"Grade(id={self.id}, score={self.score}, student_id={self.student_id})"
