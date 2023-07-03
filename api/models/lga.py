from .dbUtil import db


class Lga(db.Model):
    __tablename__ = "lgas"

    id = db.Column(db.Integer, db.Sequence('lgas_id_seq'), primary_key=True, unique=True)
    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)