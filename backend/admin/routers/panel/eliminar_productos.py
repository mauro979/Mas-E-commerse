from fastapi import APIRouter, HTTPException
from admin.routers.panel.agg_product import data
from bson import ObjectId

router = APIRouter()

@router.delete("/productos/delete/{id}",status_code=200)
async def eliminar_productos(id : str):
    
    try:
        if data.find_one_and_delete({"_id" : ObjectId(id)}):
            return {"detail" : "el producto fue eliminado correctamente"}
        else:
            raise HTTPException(
                status_code=404,
                detail="Al parecer el archivo solicitado no existe"
            )
    except:
        raise HTTPException(
            status_code=404,
            detail="al parecer hubo un error"
        )