from repositories.inventory import InventoryRepository
from common import schema


class InventoryComponent:
    @staticmethod
    def get_inventories(db):
        return InventoryRepository.get_inventories(db)

    @staticmethod
    def get_inventory_by_id(id_, db):
        return InventoryRepository.get_inventory_by_id(id_, db)

    @staticmethod
    def create_inventory(inventory: schema.Inventory, db):

        return InventoryRepository.create_inventory(inventory_info=inventory, db=db)

    @staticmethod
    def update_inventory(inventory_id, inventory: schema.Inventory, db):
        return InventoryRepository.update_inventory(inventory_id=inventory_id,
                                                    inventory_info=inventory, db=db)
