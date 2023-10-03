from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from common import schema
from components.order import OrderComponent
from services.database import get_db


router = APIRouter(
    prefix='/order',
    tags=['Orders'],
    dependencies=[],
    responses={}
)


@router.get('/')
async def get_all_orders(db: Session = Depends(get_db)):
    return OrderComponent.get_orders(db)


@router.get('/{order_id}')
async def get_order(order_id, db: Session = Depends(get_db)):
    return OrderComponent.get_order_by_id(order_id, db)


@router.post('/')
async def create_order(request: schema.Order, db: Session = Depends(get_db)):
    try:
        return OrderComponent.create_order(order_info=request, db=db)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
