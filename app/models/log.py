from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import TIMESTAMP, ForeignKey, text as sa_text
from app.models import db
from app.models.model_mixin import ModelMixin

class Log():
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    timestamp = db.Column(db.DateTime, db.func.current_timestamp(), nullable=False)
    

class UserLog(ModelMixin, Log):
    __tablename__ = 'user_log'
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id', ), nullable=False)  
    user_status = db.Column(nullable=False)

class ApplicationLog(ModelMixin, Log):
    __tablename__ = 'application_log'
    application_id = db.Column(UUID(as_uuid=True), db.ForeignKey('app.id', ), nullable=False)  
    application_status = db.Column(nullable=False)

class ProjectLog(ModelMixin, Log):
    __tablename__ = 'project_log'
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey('project.id'), nullable=False)
    project_status = db.Column(nullable=False)

class ClusterLog(ModelMixin, Log):
    __tablename__ = 'cluster_log'
    cluster_id = db.Column(UUID(as_uuid=True), db.ForeignKey('cluster.id'), nullable=False)
    cluster_status = db.Column(db.Integer, nullable=False)

class NodeLog(ModelMixin, Log):
    __tablename__ = 'node_log'
    node_id = db.Column(UUID(as_uuid=True), db.ForeignKey('cluster.id'), nullable=False)
    node_status = db.Column(db.Integer, nullable=False)