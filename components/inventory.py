from repositories.inventory import InventoryRepository
from common import schema


class InventoryComponent:
    @staticmethod
    def get_inventories(db):
        return InventoryRepository.get_inventories(db)

    @staticmethod
    def create_inventory(inventory: schema.Inventory, db):

        return InventoryRepository.create_inventory(inventory_info=inventory, db=db)
