from datetime import date
from typing import Any
from typing_extensions import Self

from pydantic import BaseModel, field_validator

class User(BaseModel):
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    lg: str
    pswd: str

    @field_validator('pswd', mode='before')
    def validate(cls, value: Any):
        if len(value) < 5:
            print('Пароль должен состоять из более 5 символов!')
            exit()
        is_upper = False
        is_digit = False
        for i in value:
            if i.isupper():
                is_upper = True
            if i.isdigit():
                 is_digit = True

        if not is_upper:
            print('Нужна хотя бы одна заглавная буква')
            exit()
        elif not is_digit:
            print('Нужна хотя бы одна цифра')
