from app.models import db
from sqlalchemy.dialects.postgresql import UUID
from app.models.model_mixin import ModelMixin


class ProjectCluster(ModelMixin):
    _tablename_ = "project_clusters"

    id = db.Column(db.Integer, primary_key=True)
    cluster_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'clusters.id'), nullable=False)
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'Projects.id'), nullable=False)
