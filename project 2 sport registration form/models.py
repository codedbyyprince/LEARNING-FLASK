from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sport = db.Column(db.String(80), nullable=False)  # removed unique=True for sport

    def __repr__(self):
        return f"<User {self.name}>"
