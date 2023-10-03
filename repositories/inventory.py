from datetime import datetime

from sqlalchemy.orm import Session
from common import schema
from common.models import Inventory


class InventoryRepository:
    @staticmethod
    def get_inventories(db: Session):
        return db.query(Inventory).all()

    @staticmethod
    def get_inventory_by_id(id_: int, db: Session):
        return db.query(Inventory).filter(Inventory.id == id_).one_or_none()

    @staticmethod
    def create_inventory(inventory_info: schema.Inventory, db: Session):
        inventory = Inventory(
            product_id=inventory_info.product_id,
            stock_id=inventory_info.stock_id,
            no_of_items_available=inventory_info.no_of_items_available,
            manufacture_date=inventory_info.manufacture_date,
            expiry_date=inventory_info.expiry_date,
            retail_price=inventory_info.retail_price,
            invoice_price=inventory_info.invoice_price,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.add(inventory)
        db.commit()
        db.refresh(inventory)
        return inventory

