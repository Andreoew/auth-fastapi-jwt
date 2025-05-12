import re
from pydantic import BaseModel, field_validator


# class User(BaseModel):
#     username: str
#     password: str
#     email: Optional[str]

#     @field_validator('username')
#     @classmethod
#     def validate_username(cls, value):
#         if not re.match('^([a-z]|[0-9]|@)+$', value):
#             raise ValueError('Username format invalid')
#         return value
    
#     @field_validator('email')
#     @classmethod
#     def validate_email(cls, value):
#         if not re.match('^[\w\.-]+@[\w\.-]+\.\w+$', value):  
#             raise ValueError('Email format invalid')
#         return value
    
class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    
    @field_validator('username')
    # @classmethod
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username format invalid')
        return value
    
    @field_validator('email')
    # @classmethod
    def validate_email(cls, value):
        if not re.match('^[\w\.-]+@[\w\.-]+\.\w+$', value):  
            raise ValueError('Email format invalid')
        return value
    
class UserLogin(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username format invalid')
        return value
    