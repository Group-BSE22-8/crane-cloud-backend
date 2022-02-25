from unicodedata import name
from marshmallow import Schema, fields, validate
from app.helpers.age_utility import get_item_age
from app.models import clusters


class ProjectClustersInputSchema(Schema):
    cluster_id = fields.UUID()


class ProjectClustersOutputSchema(Schema):
    id = fields.UUID()
    name = fields.String()


class ProjectSchema(Schema):

    id = fields.UUID(dump_only=True)
    name = fields.String(required=True, error_message={
        "required": "name is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='name should be a valid string'
            ),
    ])
    owner_id = fields.UUID(required=True, error_message={
        "required": "owner_id is required"
    })
    cluster_id = fields.UUID(required=True, error_message={
        "required": "cluster_id is required"
    })
    description = fields.String()
    organisation = fields.String()
    project_type = fields.String()
    date_created = fields.Date(dump_only=True)
    age = fields.Method("get_age", dump_only=True)
    is_multicluster = fields.Boolean()

    project_clusters = fields.Nested(
        "ProjectClustersInputSchema", many=True, load_only=True)

    def get_age(self, obj):
        return get_item_age(obj.date_created)


class ProjectDetailsSchema(ProjectSchema):
    clusters = fields.Nested("ProjectClustersOutputSchema",
                             many=True, dump_only=True)
