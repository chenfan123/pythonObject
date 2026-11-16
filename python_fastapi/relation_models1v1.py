# 关联关系模型（1对1），供 Tortoise / aerich 导入
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

