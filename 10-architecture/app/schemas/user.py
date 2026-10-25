from pydantic import BaseModel, ConfigDict, Field


class UserCreateDTO(BaseModel):
    email: str = Field(min_length=3, max_length=320)
    password: str = Field(min_length=8, max_length=128)


class UserEmailUpdateDTO(BaseModel):
    """本接口当前只允许局部修改用户邮箱。"""

    email: str = Field(min_length=3, max_length=320)


class UserResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str


class UserPageDTO(BaseModel):
    items: list[UserResponseDTO]
    total: int
    offset: int
    limit: int
