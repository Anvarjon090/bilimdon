from datetime import date
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    last_name: str
    first_name: str
    username: str 
    birthdate: date

dummy_data = {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "birthdate": date(year=2000, month=1, day=1),
}

user = UserSchema(**dummy_data)
user_dict = user.model_dump()
user_dict['is_user'] = True
print(user_dict)