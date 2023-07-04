from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app import db
from app.models.product_model import Product

class ProductSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Product
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    productDescription = fields.String(required=True)
    productBrand = fields.String(required=True)
    price = fields.Number(required=True)
    user_id = fields.Integer(required=True)