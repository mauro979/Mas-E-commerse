from fastapi import APIRouter, status, HTTPException
from admin.routers.login.create_account_admin import company_info_db as data

router = APIRouter()

@router.get("/logo",status_code=200)
async def obtener_logo():
    logo_doc = data.find_one({})
    if logo_doc and "logo" in logo_doc:
        return {"logo" : logo_doc["logo"]}

    raise HTTPException(
        status_code=status.HTTP_424_FAILED_DEPENDENCY,
        detail="No se ha podido cargar el logo"
    )
