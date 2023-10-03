from datetime import datetime

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_, func
from common import schema
from common.models import Order, OrderItem, Inventory, Product, ProductCategory
from repositories.inventory import InventoryRepository


class OrderRepository:
    @staticmethod
    def get_orders(db: Session):
        return db.query(Order).all()

    @staticmethod
    def get_orders_in_dates(db: Session, start_date, end_date, product_filter=None, category_filter=None):
        query = db.query(Order)

        if start_date and end_date:
            query = query.filter(and_(func.date(Order.updated_at) >= start_date,
                                      func.date(Order.updated_at) <= end_date))
        if product_filter or category_filter:
            query = query.join(OrderItem).join(Inventory).join(Product).options(joinedload(Order.order_items, OrderItem.inventory, Inventory.product)).filter(
                Product.id == product_filter
            )
            if category_filter:
                query = query.filter(ProductCategory.id == category_filter)
        return query.all()

    @staticmethod
    def get_order_by_id(id_, db: Session):
        return db.query(Order).filter(Order.id == id_).one_or_none()

    @staticmethod
    def create_order(order_info: schema.Order, db: Session):
        new_order = Order(
            state=order_info.state,
            shipping_charges=order_info.shipping_charges
        )
        total_price = 0
        total_invoice_rate = 0
        for item in order_info.items:
            order_item = OrderItem(
                no_of_items=item.no_of_items,
                inventory_id=item.inventory_id,
                order_id=new_order.id
            )
            inventory = InventoryRepository.get_inventory_by_id(item.inventory_id, db)
            total_price += inventory.retail_price * item.no_of_items
            total_invoice_rate += inventory.invoice_price * item.no_of_items
            db.add(order_item)
        print("prices are ")
        new_order.total_amount = total_price
        new_order.total_cost = total_invoice_rate
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order


