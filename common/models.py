from common.base_model import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Float, Enum
from sqlalchemy.orm import relationship, backref

from constants.database import UserStatus, OrderState


class Brand(Base):
    __tablename__ = 'brand'

    name = Column('name', String(20), nullable=False)


class ProductCategory(Base):
    __tablename__ = 'product_category'

    name = Column('name', String(20))
    code = Column('code', String(40), nullable=False)


class Product(Base):
    __tablename__ = 'product'

    name = Column('name', String(20))
    brand_id = Column('brand_id', ForeignKey('brand.id', onupdate='cascade', ondelete='cascade'))
    category_id = Column('category_id', ForeignKey('product_category.id', onupdate='cascade', ondelete='cascade'))

    brand = relationship('Brand', backref=backref('product', uselist=True))
    category = relationship('ProductCategory', backref=backref('products', uselist=True))


class Stock(Base):
    __tablename__ = 'stock'

    arrived_at = Column('arrived_ata', DateTime, nullable=False)


class Inventory(Base):
    __tablename__ = 'inventory'

    product_id = Column('product_id', ForeignKey('product.id', onupdate='cascade', ondelete='cascade'),
                        nullable=False)
    stock_id = Column('stock_id', ForeignKey('stock.id', onupdate='cascade', ondelete='cascade'),
                      nullable=False)
    no_of_items_available = Column('no_of_items_available', Integer, nullable=False)
    manufacture_date = Column('manufacture_date', DateTime, nullable=False)
    expiry_date = Column('expiry_date', DateTime, nullable=False)
    retail_price = Column('retail_price', Float, nullable=False)
    invoice_price = Column('invoice_price', Float, nullable=False)


class UserAddress(Base):
    __tablename__ = 'address'

    house_no = Column('house_no', String(20), nullable=False)
    street = Column('street', String(50), nullable=False)
    city = Column('city', String(30), nullable=False)
    country = Column('country', String(30), nullable=False)


class User(Base):
    __tablename__ = 'user'

    name = Column('name', String(50), nullable=False)
    address_id = Column('address_id', ForeignKey('address.id', onupdate='cascade', ondelete='cascade'),
                        nullable=False)
    email = Column('email', String(20))
    phone = Column('phone', String(15))
    status = Column('status', Enum(*UserStatus.as_list()))
 

class Order(Base):
    __tablename__ = 'order'

    state = Column('state', Enum(*OrderState.as_list()), nullable=False)
    user_id = Column('user_id', ForeignKey('user.id', onupdate='cascade', ondelete='cascade'),
                     nullable=False)
    shipping_charges = Column('shipping_charges', Float, nullable=False)
    total_amount = Column('total_amount', Float, nullable=False)


class OrderItem(Base):
    __tablename__ = 'order_item'

    no_of_items = Column('no_of_items', Integer, nullable=False)
    inventory_id = Column('inventory_id', ForeignKey('inventory.id', onupdate='cascade', ondelete='cascade'),
                          nullable=False)
    order_id = Column('order_id', ForeignKey('order.id', onupdate='cascade', ondelete='cascade'),
                      nullable=False)

