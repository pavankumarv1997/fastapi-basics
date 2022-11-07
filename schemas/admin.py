from pydantic import BaseModel


class Admin(BaseModel):
    name: str
    email: str
    phone: int
    password: str
    level: int
    login_status: int
