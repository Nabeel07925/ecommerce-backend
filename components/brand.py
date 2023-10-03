from repositories.brand import BrandRepository
from common import schema
from repositories.product_category import ProductCategoryRepository


class BrandComponent:
    @staticmethod
    def get_brands(db):
        return BrandRepository.get_brands(db)

    @staticmethod
    def get_brand(brand_id, db):
        return BrandRepository.get_brand(
            brand_id=brand_id,
            db=db
        )

    @staticmethod
    def create_brand(brand_info: schema.Brand, db):
        return BrandRepository.create_brand(
            brand_info=brand_info,
            db=db
        )
