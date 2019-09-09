from app import db
from models.user import User
from models.organisation import Organisation

class OrganisationMembers(db.Model):

    _tablename_ = "organisation_members"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey(User.id))
    organisation_id = db.Column("orgainsation_id", db.Integer, db.ForeignKey(Organisation.id))

    def __init__(self, user_id, organisation_id):
        """ initialize with name, member and namespace """
        self.user_id = user_id
        self.organisation_id = organisation_id


    def save(self):
        db.session.add(self)
        db.session.commit()