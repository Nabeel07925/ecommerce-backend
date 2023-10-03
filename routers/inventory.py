from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from common import schema
from components.inventory import InventoryComponent
from services.database import get_db


router = APIRouter(
    prefix='/inventory',
    tags=['Inventory'],
    dependencies=[],
    responses={}
)


@router.get('/')
async def get_all_inventory(db: Session = Depends(get_db)):
    return InventoryComponent.get_inventories(db)


@router.get('/{inventory_id}')
async def get_all_inventory(inventory_id, db: Session = Depends(get_db)):
    return InventoryComponent.get_inventory_by_id(inventory_id, db)


@router.post('/')
async def create_inventory(request: schema.Inventory, db: Session = Depends(get_db)):
    try:
        return InventoryComponent.create_inventory(inventory=request, db=db)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@router.put('/{inventory_id}')
async def update_inventory(inventory_id: int, request: schema.Inventory, db: Session = Depends(get_db)):
    try:
        return InventoryComponent.update_inventory(inventory_id=inventory_id,
                                                   inventory=request, db=db)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
