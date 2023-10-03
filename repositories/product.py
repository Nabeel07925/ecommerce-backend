from sqlalchemy.orm import Session
from common import schema
from common.models import Product


class ProductRepository:
    @staticmethod
    def get_products(db: Session):
        return db.query(Product).all()

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

