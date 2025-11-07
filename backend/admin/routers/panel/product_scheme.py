from pydantic import BaseModel, Field

class Product(BaseModel):
    name : str
    price :  str
    description : str
    image : str
    stock : int

    @property
    def precio_formateado(self) -> str:
        return f"{float(self.price):.2f}"

class Product_db(Product):
    id: str = Field(..., alias="_id")