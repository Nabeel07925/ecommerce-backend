from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from common import schema
from components.order import OrderComponent
from components.revenue import RevenueComponent
from services.database import get_db


router = APIRouter(
    prefix='/revenue',
    tags=['Revenue'],
    dependencies=[],
    responses={}
)


@router.get('/')
async def get_revenue(start_date=None, end_date=None, product_id=None, category_id=None, db: Session = Depends(get_db)):
    return RevenueComponent.get_revenue_in_time_duration(
        start_date=start_date,
        end_date=end_date,
        db=db,
        product_id=product_id,
        category_id=category_id
    )
