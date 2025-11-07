from fastapi import APIRouter, HTTPException, status, Response
from user.user_scheme import Login_user
from admin.routers.login.create_account_admin import user_db, pwd_context, SECRET_KEY, ALGORITHM, EXP_TOKEN_DIAS
from datetime import datetime, timedelta
from jose import jwt

router = APIRouter()

@router.post("/user/login",status_code=status.HTTP_200_OK)
async def login_user(login : Login_user, response : Response):
        try:
            user = user_db.find_one({"email" : login.email})
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Al parecer hubo un error al establecer conexion con nuestros servidores, por favor intentelo mas tarde"
            )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"el usuario {login.username} no existe"
            )
        if not user["password"] or not login.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="el usuario no tiene contracena registrada"
            )
        if not pwd_context.verify(login.password , user["password"])  or user["email"] != login.email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="la palabra de pase o el email no es valido"
            )
        payload = {
                "sub" : user["username"],
                "role" : user["admin"],
                "id" : str(user["_id"]),
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