from repositories.product import ProductRepository
from common import schema


class ProductComponent:
    @staticmethod
    def get_products(db):
        return ProductRepository.get_products(db)

    @staticmethod
    def get_product_by_id(id_, db):
        return ProductRepository.get_product_by_id(id_, db)

    @staticmethod
    def create_product(product_info: schema.Product, db):

        return ProductRepository.create_product(product_info=product_info, db=db)
