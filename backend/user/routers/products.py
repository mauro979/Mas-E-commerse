from fastapi import APIRouter, HTTPException, status
from admin.routers.panel.agg_product import data
from admin.routers.panel.product_scheme import Product_db

router = APIRouter()

@router.get("/productos/chakepoint/{cantidad}",status_code=status.HTTP_200_OK)
async def devolver_productos(cantidad : int):
    productos = []
    productos.clear()
    encontrados = False
    for i in data.find().sort("_id",-1):
        try:
            if len(productos) == cantidad:
                break
            i["_id"] = str(i["_id"])
            productos.append(Product_db(**i))
            encontrados = True
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="al parecer hubo algun error en la comunicacion con nuestros servidores"
            )
    if not encontrados or cantidad == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay ningun producto agregado"
        )
    return {"productos" : productos}