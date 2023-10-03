from pydantic import BaseModel


class ProductCategory(BaseModel):
    name: str
    code: str


class Product(BaseModel):
    name: str
    brand_id: int
    category_id: int


class Brand(BaseModel):
    name: str
