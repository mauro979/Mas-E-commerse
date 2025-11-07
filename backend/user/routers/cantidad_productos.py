from fastapi import APIRouter, status, HTTPException
from admin.routers.panel.agg_product import data

router = APIRouter()

@router.get("/productos/cantidad",status_code=status.HTTP_200_OK)
async def cantidad_productos():
    cantidad = data.count_documents({})
    if not cantidad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no hay productos aun"
        )
    if cantidad >= 20 and cantidad < 100:
        return {"cantidad" : round(cantidad * 0.50)}
    elif cantidad >= 100 and cantidad <= 1000:
        return {"cantidad" : round(cantidad * 0.25)}
    elif cantidad > 1000:
        return {"cantidad" : round(cantidad * 0.10)}
    return {"cantidad" : cantidad}