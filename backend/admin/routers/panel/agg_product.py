from fastapi import HTTPException , status, APIRouter
from admin.routers.login.create_account_admin import db
from admin.routers.panel.product_scheme import Product

router = APIRouter()

data = db.products

@router.post("/createproducts")
async def create_product(product : Product, status_code=201):
    if not data.find_one({"name":product.name}):
        try:
            data.insert_one(product.model_dump()).inserted_id
            return {"message" : "producto agregado con exito"}
        except:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="el producto a agregar no es valido"
            )
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="el producto ya existe"
    )
    