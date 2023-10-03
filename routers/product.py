from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from common import schema
from components.product import ProductComponent
from services.database import get_db


router = APIRouter(
    prefix='/product',
    tags=['Product'],
    dependencies=[],
    responses={}
)


@router.get('/')
async def get_all_products(db: Session = Depends(get_db)):
    return ProductComponent.get_products(db)


@router.post('/')
async def create_product(request: schema.Product, db: Session = Depends(get_db)):
    try:
        return ProductComponent.create_product(product_info=request, db=db)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
