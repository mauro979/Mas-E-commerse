from fastapi import APIRouter, status, HTTPException
from admin.routers.panel.agg_product import data

router = APIRouter()

@router.get("/{solicitud}")
async def test(nombre : str, solicitud : str):
    name = nombre
    if solicitud == "maurizio":
        return nombre
    return "no"