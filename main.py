from fastapi import FastAPI
import uvicorn

from common import models
from routers import inventory, product, brand, product_category
from services.database import engine

app = FastAPI()
app.include_router(inventory.router)
app.include_router(product.router)
app.include_router(product_category.router)
app.include_router(brand.router)
models.Base.metadata.create_all(engine)

if __name__ == '__main__':
    uvicorn.run(app)
