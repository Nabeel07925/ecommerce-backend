from fastapi import APIRouter

router = APIRouter(
    prefix='/inventory',
    tags=['Inventory'],
    dependencies=[],
    responses={}
)


@router.get('/')
async def get_all_inventory():
    return [{
        'id': 1,
        'name': 'fake item'
    }]
