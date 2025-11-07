from fastapi import HTTPException , status, APIRouter, Request, Response
from jose import JWTError, jwt
from admin.routers.login.login import user_db, SECRET_KEY, ALGORITHM
from jose.exceptions import ExpiredSignatureError
from jwt.exceptions import InvalidTokenError
from bson.objectid import ObjectId

router = APIRouter()

@router.get("/tokenverificationadmin", status_code=200)
def perfil(request: Request):
      token = request.cookies.get("access_token")
      if not token:
          raise HTTPException(status_code=401, detail="No autenticado")

      try:
          payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

          user = user_db.find_one({"_id" : ObjectId(payload['id'])})

          if not user or not user["admin"]:
              raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Token inválido")
      except ExpiredSignatureError:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
      except InvalidTokenError:
          raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Token inválido")

@router.get("/cookies")
async def obtener_cookies(request : Request, response : Response):
    token = request.get("access_token")
    if not token:
          raise HTTPException(status_code=401, detail="No autenticado")
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    print(payload)
    return {"cookies":payload}