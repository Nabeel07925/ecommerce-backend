import datetime
from typing import List, Union

from pydantic import BaseModel


class ProductCategory(BaseModel):
    name: str
    code: str


class Product(BaseModel):
    name: str
    brand_id: int
    category_id: int


class Inventory(BaseModel):
    product_id: int
    stock_id: int
    no_of_items_available: int
    manufacture_date: datetime.date
    expiry_date: datetime.date
    retail_price: float
    invoice_price: float


class OrderItem(BaseModel):
    no_of_items: int
    inventory_id: int


class Order(BaseModel):
    state: str
    shipping_charges: int
    items: List[OrderItem]


class Brand(BaseModel):
    name: str


class Revenue(BaseModel):
    start_date: Union[str, None]
    end_date: Union[str, None]
    total_sales: Union[float, None]
    total_profit: Union[float, None]
