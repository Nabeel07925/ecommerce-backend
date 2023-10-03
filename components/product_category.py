from repositories.product import ProductRepository
from common import schema
from repositories.product_category import ProductCategoryRepository


class ProductCategoryComponent:
    @staticmethod
    def get_product_categories(db):
        return ProductCategoryRepository.get_product_categories(db)

    @staticmethod
    def get_product_category(category_id, db):
        return ProductCategoryRepository.get_product_category(
            category_id=category_id,
            db=db
        )

    @staticmethod
    def create_product(category_info: schema.ProductCategory, db):
        return ProductCategoryRepository.create_product_category(
            category_info=category_info,
            db=db
        )
