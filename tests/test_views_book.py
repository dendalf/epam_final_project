from library_app import app, db  # Flask instance of the API
from library_app.models.book import Book


def test_read_books():
    response = app.test_client().get('/book/list')

    assert response.status_code == 200
    with app.app_context():
        book1 = Book(title='Test title1', author_id=1, date_published='2023-03-14', price=20)
        db.session.add(book1)
        db.session.commit()
        request = app.test_client().get('/book/list?date_published_start=2023-03-13&date_published_end=2023-03-15')
        assert b'Test title1' in request.data
        assert b'2023-03-14' in request.data
        assert b'20' in request.data
        db.session.delete(book1)
        db.session.commit()


def test_detail():

    with app.app_context():
        book1 = Book(title='Test title1', author_id=1, date_published='2023-03-14', price=20)
        db.session.add(book1)
        db.session.commit()
        response = app.test_client().get(f'/book/detail/{book1.id}')
        assert response.status_code == 200
        assert b'Test title1' in response.data
        assert b'2023-03-14' in response.data
        assert b'20' in response.data
        db.session.delete(book1)
        db.session.commit()
        db.session.close()
        response = app.test_client().get(f'/book/detail/{book1.id}')
        assert b'Page not found' in response.data
