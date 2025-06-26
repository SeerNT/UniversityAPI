from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class SchemaMajor(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    major_name: str = Field(..., description="Название факультета")
    major_description: Optional[str] = Field(None, description="Описание факультета")
    count_students: int = Field(0, description="Кол-во студентов")

class SchemaMajorAdd(BaseModel):
    major_name: str = Field(..., description="Название факультета")
    major_description: str = Field(None, description="Описание факультета")
    count_students: int = Field(0, description="Кол-во студентов")

class SchemaMajorUpdate(BaseModel):
    major_name: str = Field(..., description="Название факультета")
    major_description: str = Field(None, description="Описание факультета")
