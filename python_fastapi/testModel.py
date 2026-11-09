from tortoise.models import Model
from tortoise.fields import CharField, DatetimeField, BooleanField
from tortoise.indexes import Index


class Test(Model):
    id = CharField(max_length=36, pk=True)  # 主键, UUID 字符串
    username = CharField(max_length=50, unique=True)  # 用户名, 唯一
    email = CharField(max_length=255, unique=True)  # 邮箱, 唯一
    is_active = BooleanField(default=True)  # 是否激活
    created_at = DatetimeField(auto_now_add=True)  # 创建时间
    updated_at = DatetimeField(auto_now=True)  # 更新时间

    class Meta:
        table = "test_table"  # 自定义表名
        ordering = ["-created_at"]  # 默认按创建时间降序排序
        unique_together = ("username", "email")  # 联合唯一
        # 创建索引
        indexes = [
            Index(fields=["username", "email"]),  # 创建联合索引
        ]

    def __str__(self):
        return self.username


"""
aerich init -t settings.TEST_ORM 只写配置，生成/更新pyproject.toml文件,创建空的migrations/目录
aerich init-db 根据 ORM 模型在数据库里建表，并生成首个迁移文件。叫「迁移文件」，是因为它们记录的是数据库结构怎么从旧版本变到新版本，像一份变更脚本，不是一次性建表的临时文件。
"""
