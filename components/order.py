from repositories.order import OrderRepository
from common import schema
from sqlalchemy.orm import Session


class OrderComponent:
    @staticmethod
    def get_orders(db):
        return OrderRepository.get_orders(db)

    @staticmethod
    def get_order_by_id(id_: int, db: Session):
        return OrderRepository.get_order_by_id(id_, db)

    @staticmethod
    def create_order(order_info: schema.Order, db):
        return OrderRepository.create_order(order_info=order_info, db=db)
