from app.models import db
from sqlalchemy.dialects.postgresql import UUID
from app.models.model_mixin import ModelMixin
from sqlalchemy import text as sa_text


class ProjectCluster(ModelMixin):
    _tablename_ = "project_clusters"
    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   server_default=sa_text("uuid_generate_v4()"))
    cluster_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'clusters.id'), nullable=False)
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'project.id'), nullable=False)
