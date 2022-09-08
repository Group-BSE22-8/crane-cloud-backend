from marshmallow import Schema, fields
from app.helpers.age_utility import get_item_age


class StatusSchema(Schema):

    id = fields.String(required=True)
    user_id = fields.String(required=True)
    status = fields.Int(required=True)
    comment = fields.String(required=True)

    def get_age(self, obj):
        return get_item_age(obj.date_created)
