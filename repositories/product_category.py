from sqlalchemy.orm import Session
from common import schema
from common.models import ProductCategory


class ProductCategoryRepository:
    @staticmethod
    def get_product_categories(db: Session):
        return db.query(ProductCategory).all()

    @staticmethod
    def get_product_category(category_id: int, db: Session):
        return db.query(ProductCategory).filter(ProductCategory.id == category_id).all()

    @staticmethod
    def create_product_category(category_info: schema.ProductCategory, db: Session):
        new_category = ProductCategory(
            name=category_info.name,
            code=category_info.code
        )
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

