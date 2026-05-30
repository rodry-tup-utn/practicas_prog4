from pydantic import BaseModel, Field, ConfigDict


class CategoryCreate(BaseModel):
    name: str = Field(min_length=3, max_length=40)
    description: str | None = Field(default=None, min_length=3, max_length=255)


class CategoryUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str | None = Field(default=None, min_length=3, max_length=40)
    description: str | None = None


class CategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None


class CategoryPaginated(BaseModel):
    items: list[CategoryRead]
    total: int


class CategoryFilters(BaseModel):
    name: str = Field(min_length=3, max_length=80)
    offset: int = 0
    limit: int = 20
