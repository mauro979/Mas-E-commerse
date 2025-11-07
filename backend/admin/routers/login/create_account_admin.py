from fastapi import HTTPException , status, APIRouter, Response
from admin.routers.login.user_admin import Admin
from pymongo import MongoClient
from passlib.context import CryptContext 
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from datetime import datetime, timedelta
from jose import jwt

router = APIRouter()

client = MongoClient()## mongodb+srv://mauriziogomezvalle5_db_user:kJRy8oplIA004w7R@cluster0.sxkgixg.mongodb.net/ ##
db = client.data
user_db = db.user
company_info_db = db.company_info

SECRET_KEY = "c2214cfd41cfe71ada8a20f3007b7b3b50eea2b9c20535475c1afb27e984bbab"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"])
token = OAuth2PasswordBearer(tokenUrl="/autentication")

EXP_TOKEN_DIAS = 15

@router.post("/CreateAccountAdmin",status_code=status.HTTP_201_CREATED)
async def Createaccount(user : Admin, response : Response):

    if user_db.count_documents(filter={"admin" : True}) == 1:
         raise HTTPException(
              status_code=status.HTTP_409_CONFLICT,
              detail="Ya existe una cuenta de administrador"
         )

    if not user_db.find_one({"email":user.email}):

        #try:
            #insertando la informacion del admin
            user.password = pwd_context.hash(str(user.password))

            admin_data = {
                "username": user.username,
                "email" : user.email,
                "password" : user.password,
                "admin" : user.admin,
            }

            user_db.insert_one(dict(admin_data)).inserted_id

            #insertando la informacion de el negocio
            company_info = {
                    "company_name" : user.company_name,
                    "logo" : user.logo
            }

            company_info_db.insert_one(company_info).inserted_id

            id_user = user_db.find_one({"email":user.email})

            if id_user is None:
                raise HTTPException(
                     status_code=status.HTTP_424_FAILED_DEPENDENCY,
                     detail="ha habido un error de autenticacion, por favor intentelo mas tarde"
                )

            payload = {
                "sub" : user.username,
                "role" : user.admin,
                "id" : str(id_user["_id"]),
                "exp" : (datetime.now() + timedelta(days=EXP_TOKEN_DIAS))
            }

            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

            response.set_cookie(
                key="access_token",
                value=token,
                httponly=True,
                secure=False,  # True en producción con HTTPS
                samesite="lax"
            )
            
        
        # except Exception as e:
            
        #     raise HTTPException(
        #     status_code=status.HTTP_400_BAD_REQUEST,
        #     detail="ha habido un error de autenticacion"
        # )
        
    else:   
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="el usuario ya existe"
        )


# from fastapi import Request

# @app.get("/perfil")
# def perfil(request: Request):
#     token = request.cookies.get("access_token")
#     if not token:
#         raise HTTPException(status_code=401, detail="No autenticado")

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token expirado")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Token inválido")

#     return {"usuario": payload["sub"], "rol": payload["role"]}