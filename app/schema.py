from pydantic import BaseModel, EmailStr

class Create_User(BaseModel):
    Name: str
    Email: str
    Password: str
    Job_Title: str | None = None