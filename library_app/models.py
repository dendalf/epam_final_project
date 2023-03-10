""" Models file for library_app """
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
        return f'{self.title} {self.author}'

    def __repr__(self):
        return f'<Book {self.id} {self.title} {self.created} {self.updated}'


class Author(db.Model):
    """ Author model """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    books = db.relationship('Book', backref='author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_avg_price(self):
        """ Calculate average price of books for 1 Author """
        if self.books:
            sum_price = 0
            for book in self.books:
                sum_price += book.price
            return round(sum_price / len(self.books))
        else:
            return 0
