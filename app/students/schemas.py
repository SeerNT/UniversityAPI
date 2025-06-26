from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict


class SchemaStudent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: date = Field(..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(..., description="Электронная почта студента")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес студента, не более 200 символов")
    enrollment_year: int = Field(..., ge=2002, description="Год поступления должен быть не меньше 2002")
    course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(None, max_length=500, description="Дополнительные заметки, не более 500 символов")
    major_id: int = Field(..., ge=1, description="ID специальности студента")
    photo: Optional[str] = Field(None, max_length=100, description="Фото студента")

    major: Optional[str] = Field(..., description="Название факультета")

    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, value):
        if value and value >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return value

class SchemaStudentAdd(BaseModel):
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50,
                           description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: date = Field(..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(..., description="Электронная почта студента")
    address: str = Field(..., min_length=10, max_length=200,
                         description="Адрес студента, не более 200 символов")
    enrollment_year: int = Field(..., ge=2002, description="Год поступления должен быть не меньше 2002")
    major_id: int = Field(..., ge=1, description="ID специальности студента")
    course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(None, max_length=500,
                                         description="Дополнительные заметки, не более 500 символов")
    photo: Optional[str] = Field(None, max_length=100, description="Фото студента")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values

class SchemaStudentUpdate(BaseModel):
    phone_number: Optional[str] = Field(description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: Optional[str] = Field(min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: Optional[str] = Field(min_length=1, max_length=50,
                           description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: Optional[date] = Field(description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: Optional[EmailStr] = Field(description="Электронная почта студента")
    address: Optional[str] = Field(min_length=10, max_length=200,
                         description="Адрес студента, не более 200 символов")
    enrollment_year: Optional[int] = Field(ge=2002, description="Год поступления должен быть не меньше 2002")
    major_id: Optional[int] = Field(ge=1, description="ID специальности студента")
    course: Optional[int] = Field(ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(None, max_length=500,
                                         description="Дополнительные заметки, не более 500 символов")
    photo: Optional[str] = Field(None, max_length=100, description="Фото студента")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values

    def to_dict(self):
        attrs =  [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
        result = {}
        for attr in attrs:
            value = getattr(self, attr)
            result.update({attr: value})
        return result