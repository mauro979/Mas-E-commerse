from fastapi import HTTPException , status, APIRouter, Request, Response
from user.user_scheme import User
from admin.routers.login.create_account_admin import user_db, pwd_context, ALGORITHM, SECRET_KEY, EXP_TOKEN_DIAS
from fastapi import Depends
from datetime import datetime, timedelta
from jose import JWTError, jwt

router = APIRouter()

@router.post("/CreateAccountUser",status_code=status.HTTP_201_CREATED)
async def Createacount(user : User, response : Response):

    if not user_db.find_one({"email":user.email}):

        #  try:
             #insertando la informacion del usuario
             user.password = pwd_context.hash(str(user.password))

             user_data = {
                 "username": user.username,
                 "email" : user.email,
                 "password" : user.password,
                 "admin" : user.admin,
             }

             user_db.insert_one(user_data).inserted_id

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
                 "exp" : datetime.now() + timedelta(days=EXP_TOKEN_DIAS)
             }

             token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

             response.set_cookie(
                 key="access_token",
                 value=token,
                 httponly=True,
                 secure=False,   #True en producción con HTTPS
                 samesite="lax",
             )
            
        
        #     except Exception as e:
            
        #       raise HTTPException(
        #       status_code=status.HTTP_400_BAD_REQUEST,
        #       detail="ha habido un error de autenticacion"
        #   )
        
    else:   
         raise HTTPException(
             status_code=status.HTTP_409_CONFLICT,
             detail="el usuario ya existe"
         )