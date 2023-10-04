from sqlalchemy.orm import Session
from common import schema
from common.models import Product


class ProductRepository:
    @staticmethod
    def get_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_product_by_id(id_: int, db: Session):
        return db.query(Product).filter(Product.id == id_).one_or_none()

    @staticmethod
    def create_product(product_info: schema.Product, db: Session):
        prod = Product(
            name=product_info.name,
            brand_id=product_info.brand_id,
            category_id=product_info.category_id
        )
        db.add(prod)
        db.commit()
        db.refresh(prod)
        return prod

