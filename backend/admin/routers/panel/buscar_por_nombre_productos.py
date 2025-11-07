from fastapi import APIRouter, status, HTTPException
from admin.routers.panel.agg_product import data

router = APIRouter()

@router.get("/productos/buscarpornombre/{nombre}",status_code=200)
async def buscar_productos_por_nombre(nombre : str):
    producto = data.find_one({"name" : nombre})

    if producto:
        diccionario = {
            "id" : str(producto["_id"]),
            "name" : str(producto["name"]),
            "price" : str(producto["price"]),
            "description" : str(producto["description"]),
            "image" : str(producto["image"]),
            "stock" : int(producto["stock"])
        }
        print("test passed")
        return {"data" : diccionario}
    else:
        raise HTTPException(
            status_code=404,
            detail=f"El producto {nombre} no existe"
        )