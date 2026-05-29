from sqlmodel import SQLModel, Field


class CategoryCreate(SQLModel):
    name: str = Field(min_length=3, max_length=40)
    description: str | None = Field(default=None, min_length=3, max_length=255)


class CategoryUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=3, max_length=40)
    description: str | None = None


class CategoryRead(SQLModel):
    id: int
    name: str
    description: str | None
