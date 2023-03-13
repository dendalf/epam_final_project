"""
This file (test_models_author.py) contains the unit tests for the author.py file.
"""
from library_app import db, app
from library_app.models.author import Author
from library_app.models.book import Book


def test_new_author():
    """
    GIVEN an Author model
    WHEN a new Author is created
    THEN check the first_name, last_name and birthdate
    """
    author = Author(first_name='Test first', last_name='Test last', birthdate='2023-03-30')
    assert author.first_name == 'Test first'
    assert author.last_name == 'Test last'
    assert author.birthdate == '2023-03-30'
    assert author.__str__() == 'Test first Test last'


def test_avg_price():
    """
        GIVEN an Author model
        WHEN a new Author is created
        THEN check the function get_avg_price
    """
    with app.app_context():
        author = Author(first_name='Test first', last_name='Test last', birthdate='2023-03-30')
        db.session.add(author)
        db.session.commit()
        book1 = Book(title='Test title1', author_id=author.id, date_published='2023-03-30', price=20)
        book2 = Book(title='Test title2', author_id=author.id, date_published='2023-03-30', price=80)
        db.session.add(book1)
        db.session.add(book2)
        db.session.commit()
        assert author.get_avg_price() == 50
        db.session.delete(author)
        db.session.delete(book1)
        db.session.delete(book2)
        db.session.commit()


def test_avg_price_zero_books():
    """
        GIVEN an Author model
        WHEN a new Author is created
        THEN check the function get_avg_price
    """
    with app.app_context():
        author = Author(first_name='Test first', last_name='Test last', birthdate='2023-03-30')
        db.session.add(author)
        db.session.commit()
        assert author.get_avg_price() == 0
        db.session.delete(author)
        db.session.commit()
