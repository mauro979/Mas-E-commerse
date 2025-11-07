from fastapi import APIRouter, HTTPException, status, Response
from admin.routers.login.user_admin import User_login
from admin.routers.login.create_account_admin import user_db, SECRET_KEY, EXP_TOKEN_DIAS, ALGORITHM, pwd_context
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/loginadmin",status_code=status.HTTP_200_OK)
async def login(admin : User_login, response : Response):

    try:
        user = user_db.find_one({"username" : admin.username})
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Al parecer hubo un error al establecer conexion con nuestros servidores, por favor intentelo mas tarde"
        )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"el usuario {admin.username} no existe"
        )
    if not admin.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="el usuario no tiene contracena registrada"
        )
    if not pwd_context.verify(admin.password, user["password"]) or user["email"] != admin.email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="la palabra de pase o el email no es valido"
        )
    elif not user["admin"] :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"El usuario {admin.username} no tiene permisos de administrador"
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
    