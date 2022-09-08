from marshmallow import Schema, fields
from app.helpers.age_utility import get_item_age


class AppLogsSchema(Schema):

    id = fields.UUID(dump_only=True)
    app_id = fields.UUID(dump_only=True)
    action = fields.String()
    comment = fields.String()
    performed_by = fields.UUID(dump_only=True)
    date_created = fields.Date(dump_only=True)

    def get_age(self, obj):
        return get_item_age(obj.date_created)


class ProjectLogsSchema(Schema):

    id = fields.UUID(dump_only=True)
    project_id = fields.UUID(dump_only=True)
    action = fields.String()
    comment = fields.String()
    performed_by = fields.UUID(dump_only=True)
    date_created = fields.Date(dump_only=True)


class UserLogsSchema(Schema):

    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(dump_only=True)
    action = fields.String()
    comment = fields.String()
    performed_by = fields.UUID(dump_only=True)
    date_created = fields.Date(dump_only=True)

    def get_age(self, obj):
        return get_item_age(obj.date_created)
