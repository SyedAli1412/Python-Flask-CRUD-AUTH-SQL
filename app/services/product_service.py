from app.models.product_model import Product
from app import db

class ProductService:
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(id):
        return Product.query.get(id)

    @staticmethod
    def create_product(data):
        product = Product(**data)
        return product.create()

    @staticmethod
    def update_product(product, data):
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product):
        db.session.delete(product)
        db.session.commit()
