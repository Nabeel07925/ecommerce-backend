from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from common import schema
from components.product import ProductComponent
from components.product_category import ProductCategoryComponent
from services.database import get_db


router = APIRouter(
    prefix='/product-category',
    tags=['Product Category'],
    dependencies=[],
    responses={}
)

@router.get('/')
async def get_all_product_categories(db: Session = Depends(get_db)):
    return ProductCategoryComponent.get_product_categories(db)


@router.post('/')
async def create_product_category(request: schema.ProductCategory, db: Session = Depends(get_db)):
    try:
        return ProductCategoryComponent.create_product(category_info=request, db=db)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
