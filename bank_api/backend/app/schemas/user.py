from pydantic import BaseModel, Field
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    user_name: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    user_name: str
    password: str = Field(
            min_length=8,
            max_length=20,
            regex=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])"
        )


class UserUpdate(schemas.BaseUserUpdate):
    pass
