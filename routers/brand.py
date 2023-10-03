from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from common import schema
from components.brand import BrandComponent
from components.product import ProductComponent
from services.database import get_db


router = APIRouter(
    prefix='/brand',
    tags=['Brand'],
    dependencies=[],
    responses={}
)


@router.get('/')
async def get_all_brands(db: Session = Depends(get_db)):
    return BrandComponent.get_brands(db)


@router.post('/')
async def create_brand(request: schema.Brand, db: Session = Depends(get_db)):
    try:
        return BrandComponent.create_brand(brand_info=request, db=db)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
