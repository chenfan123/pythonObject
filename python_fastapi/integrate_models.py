from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=64)
    age = fields.IntField(null=True)  # 与 UserSchema.age 对齐

    class Meta:
        table = "users"

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, age={self.age})"
