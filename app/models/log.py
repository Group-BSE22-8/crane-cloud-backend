from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from app.models import db
from app.models.model_mixin import ModelMixin


class UserLog(ModelMixin):
    __tablename__ = 'user_logs'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(256), nullable=True)
    performed_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())



class ProjectLog(ModelMixin):
    __tablename__ = 'project_logs'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey('project.id'), nullable=False)
    action = db.Column(db.String(256), nullable=True)
    performed_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


class AppLog(ModelMixin):
    __tablename__ = 'app_logs'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    app_id = db.Column(UUID(as_uuid=True), db.ForeignKey('app.id'), nullable=False)
    action = db.Column(db.String(256), nullable=True)
    performed_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


class ClusterLog(ModelMixin):
    __tablename__ = 'cluster_logs'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    cluster_id = db.Column(UUID(as_uuid=True), db.ForeignKey('clusters.id'), nullable=False)
    status = db.Column(db.String(256), nullable=True)


class NodeLog(ModelMixin):
    __tablename__ = 'node_logs'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    node_id = db.Column(UUID(as_uuid=True), db.ForeignKey('app.id'), nullable=False)
    action = db.Column(db.String(256), nullable=True)
    performed_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
