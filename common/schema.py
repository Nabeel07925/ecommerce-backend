import datetime
from typing import List
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
    start_date: str
    end_date: str
    total_sales: float
    total_profit: float
