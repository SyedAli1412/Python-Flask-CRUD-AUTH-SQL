from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app.models.models import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password", "confirm_password")

    id = fields.Integer(dump_only=True)
    name = fields.String()
    email = fields.Email(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)

