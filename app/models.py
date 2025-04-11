# Add any model classes for Flask-SQLAlchemy here
from . import db
class Movie(db.Model):
    
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    poster = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False )
