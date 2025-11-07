from pydantic import BaseModel

class User(BaseModel):
    username : str
    email : str
    admin : bool

class User_pass(User):
    password : str

class User_login(User_pass):
    admin : None = None
    

class Admin(User_pass):
    company_name : str
    logo : str

# #terminar la separracion de la compañia de la del admin
# class CompanyInfo(User):
#     company_name : str
#     logo : str