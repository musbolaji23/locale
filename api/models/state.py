from .dbUtil import db


class State(db.Model):
    __tablename__ = "states"

    id = db.Column(db.Integer, db.Sequence('states_id_seq'), primary_key=True, unique=True)
    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    capital = db.Column(db.String(255), nullable=False)
    governor = db.Column(db.String(255), nullable=False)
    slogan = db.Column(db.String(255), nullable=False)
    no_of_lgas = db.Column(db.Integer, nullable=False)