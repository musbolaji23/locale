from .dbUtil import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    api_key = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.email}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
   