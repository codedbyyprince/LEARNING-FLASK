# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'  # optional but clean
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
