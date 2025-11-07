from pydantic import BaseModel

class User(BaseModel):
    username : str
    email : str
    password : str
    admin : bool

class Login_user(User):
    admin : None = None

#modelo de usuario sin permisos de administrador