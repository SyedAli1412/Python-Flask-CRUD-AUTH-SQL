from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app.models.models import Message


class MessageSchema(SQLAlchemySchema):
    class Meta:
        model = Message
        load_instance = True

    id = fields.Integer(dump_only=True)
    message = fields.String(required=True)
    sender_id = fields.Integer(required=True)
    receiver_id = fields.Integer(required=True)
