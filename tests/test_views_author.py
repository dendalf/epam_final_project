from library_app import app, db  # Flask instance of the API
from library_app.models.author import Author


def test_list_author():
    response = app.test_client().get('/author/list')

    assert response.status_code == 200
    with app.app_context():
        author1 = Author(first_name='Test name1', last_name='Test name2', birthdate='2023-03-14')
        db.session.add(author1)
        db.session.commit()
        response = app.test_client().get('/author/list')
        assert b'Test name1' in response.data
        assert b'Test name2' in response.data
        assert b'2023-03-14' in response.data
        db.session.delete(author1)
        db.session.commit()


def test_detail():

    with app.app_context():
        author1 = Author(first_name='Test name1', last_name='Test name2', birthdate='2023-03-14')
        db.session.add(author1)
        db.session.commit()
        response = app.test_client().get(f'/author/detail/{author1.id}')
        assert response.status_code == 200
        assert b'Test name1' in response.data
        assert b'Test name2' in response.data
        assert b'2023-03-14' in response.data
        db.session.delete(author1)
        db.session.commit()
        db.session.close()
        response = app.test_client().get(f'/author/detail/{author1.id}')
        assert b'Page not found' in response.data
