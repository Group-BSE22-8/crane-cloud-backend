from marshmallow import Schema, fields, validate
from app.helpers.age_utility import get_item_age

class UserLogSchema(Schema):
    id = fields.UUID(dump_only=True)
    user_id = fields.UUID(dump_only=True)
    user_status = fields.String(dump_only=True)

class ApplicationLogSchema(Schema):
    id = fields.UUID(dump_only=True)
    application_id = fields.UUID(dump_only=True)
    application_status = fields.String(dump_only=True)
    

class ProjectLogSchema(Schema):
    id = fields.UUID(dump_only=True)
    project_id = fields.UUID(dump_only=True)
    project_status = fields.String(dump_only=True)
    
class ClusterLogSchema(Schema):
    id = fields.UUID(dump_only=True)
    cluster_id = fields.UUID(dump_only=True)
    cluster_status = fields.String(dump_only=True)

class NodeLogSchema(Schema):
    id = fields.UUID(dump_only=True)
    node_id = fields.String(dump_only=True)
    node_status = fields.String(dump_only=True)


