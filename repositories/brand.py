from sqlalchemy.orm import Session
from common import schema
from common.models import Brand


class BrandRepository:
    @staticmethod
    def get_brands(db: Session):
        return db.query(Brand).all()

    @staticmethod
    def get_brand(brand_id: int, db: Session):
        return db.query(Brand).filter(Brand.id == brand_id).one_or_none()

    @staticmethod
    def create_brand(brand_info: schema.Brand, db: Session):
        new_brand = Brand(
            name=brand_info.name
        )
        db.add(new_brand)
        db.commit()
        db.refresh(new_brand)
        return new_brand

