# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Show {self.title} (Rating: {self.rating})>"