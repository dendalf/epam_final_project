""" Book models file for library_app """
# pylint: disable=no-else-return
from datetime import datetime
from library_app import db


class Book(db.Model):
    """ Book model """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    date_published = db.Column(db.Date, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'Book {self.id} {self.title} {self.created} {self.updated}'
