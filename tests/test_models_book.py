"""
This file (test_models_book.py) contains the unit tests for the book.py file.
"""

from library_app.models.book import Book


def test_new_book():
    """
    GIVEN a Book model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    book = Book(title='Test title', author_id=1, date_published='2023-03-30', price=20)
    assert book.title == 'Test title'
    assert book.author_id == 1
    assert book.__repr__() == f'Book {book.id} Test title {book.created} {book.updated}'
    assert book.date_published == '2023-03-30'
    assert book.price == 20

