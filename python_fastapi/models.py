from tortoise import fields, models
from tortoise.indexes import Index


class User(models.Model):
    id = fields.CharField(max_length=36, pk=True)  # 主键, UUID 字符串
    username = fields.CharField(max_length=50, unique=True)  # 用户名, 唯一
    email = fields.CharField(max_length=255, unique=True)  # 邮箱, 唯一
    is_active = fields.BooleanField(default=True)  # 是否激活
    created_at = fields.DatetimeField(auto_now_add=True)  # 创建时间
    updated_at = fields.DatetimeField(auto_now=True)  # 更新时间

    class Meta:
        table = "users"  # 自定义表名
        ordering = ["-created_at"]  # 默认按创建时间降序排序
        unique_together = ("username", "email")  # 联合唯一
        # 创建索引
        indexes = [
            Index(fields=["username", "email"]),  # 创建联合索引
        ]

    def __str__(self):
        return self.username


class Student(models.Model):
    """
    学生模型，包含基本信息。
    用于演示单表的增删改查操作。
    """
    id = fields.IntField(pk=True, description="学生ID，主键")
    name = fields.CharField(max_length=50, description="学生姓名")
    age = fields.IntField(null=True, description="学生年龄，可为空")
    email = fields.CharField(
        max_length=100, unique=True, null=True, description="学生邮箱，唯一"
    )

    class Meta:
        table = "students"

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Email: {self.email}"


"""
aerich init -t main19.TORTOISE_ORM # 初始化数据库
aerich init-db # 创建迁移脚本

aerich migrate --name "注释" # 迁移
aerich upgrade # 同步迁移
"""
