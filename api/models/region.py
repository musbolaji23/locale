from .dbUtil import db


class Region(db.Model):
    __tablename__ = "regions"

    id = db.Column(db.Integer, db.Sequence('regions_id_seq'), primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    no_of_states = db.Column(db.Integer, nullable=False)