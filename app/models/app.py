from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from app.models import db
from app.models.model_mixin import ModelMixin


class App(ModelMixin):
    __tablename__ = 'app'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(256), nullable=True)
    image = db.Column(db.String(256), nullable=False)
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey('project.id'), nullable=False)
    url = db.Column(db.String(256), nullable=True)
    alias = db.Column(db.String(256), nullable=True, unique=True)
    port = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    has_custom_domain = db.Column(db.Boolean, nullable=False, default=False)
