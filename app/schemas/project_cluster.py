from marshmallow import Schema, fields


class ProjectClusterSchema(Schema):

    id = fields.UUID(dump_only=True)
    cluster_id = fields.UUID(required=True)
    project_id = fields.UUID(required=True)
