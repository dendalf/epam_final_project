from flask import request, render_template, redirect, url_for

from library_app import db, app
from library_app.models import Book, Author
from library_app.forms import CreateBookForm, CreateAuthorForm, UpdateAuthorForm, DeleteAuthorForm
from library_app.forms import DeleteBookForm
from library_app.forms import UpdateBookForm


@app.route('/')
def index():
    return render_template('index.html', title='Home page', content='Welcome to Library!')


# Book views


@app.route('/book/list')
def read_books():
    books = Book.query.all()

    return render_template('list.html', title='List of books', books=books)


@app.route('/book/detail/<int:pk>')
def detail(pk):
    book = Book.query.filter_by(id=pk).first()

    if book is None:
        return render_template('index.html', title='Page not found', content='404 error')

    return render_template('detail.html', title='Book detail', book=book)


@app.route('/book/create', methods=['GET', 'POST'])
def create_book():
    form = CreateBookForm()
    form.author.choices = [("", "-----")] + [(author.id, author) for author in Author.query.all()]

    if form.validate_on_submit():
        book = Book(title=form.title.data, author_id=form.author.data, date_published=form.date_published.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('read_books'))

    return render_template('create.html', title='Create new book', form=form)


@app.route('/book/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    book = Book.query.get(pk)
    form = UpdateBookForm()
    form.author.choices = [(author.id, author) for author in Author.query.all()]

    if form.validate_on_submit():
        book.title = form.title.data
        book.author_id = form.author.data
        book.date_published = form.date_published.data
        db.session.commit()
        return redirect(url_for('read_books'))

    elif request.method == 'GET':
        form.author.default = book.author_id
        form.process()
        form.title.data = book.title
        form.date_published.data = book.date_published

    return render_template('update.html', title='Update book', book=book, form=form)


@app.route('/book/delete/<int:pk>', methods=['GET', 'POST'])
def delete(pk):
    book = Book.query.get(pk)
    form = DeleteBookForm()

    if form.validate_on_submit():
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('read_books'))

    return render_template('delete.html', title='Delete  book', book=book, form=form)


# Author views


@app.route('/author/list')
def author_list():
    authors = Author.query.all()

    return render_template('list_author.html', title='List of authors', authors=authors)


@app.route('/author/detail/<int:pk>')
def detail_author(pk):
    author = Author.query.filter_by(id=pk).first()

    if author is None:
        return render_template('index.html', title='Page not found', content='404 error')

    return render_template('detail_author.html', title='Author detail', author=author)


@app.route('/author/create', methods=['GET', 'POST'])
def create_author():
    form = CreateAuthorForm()

    if form.validate_on_submit():
        author = Author(first_name=form.first_name.data, last_name=form.last_name.data, birthdate=form.birthdate.data)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('author_list'))

    return render_template('create_author.html', title='Create new author', form=form)


@app.route('/author/update/<int:pk>', methods=['GET', 'POST'])
def update_author(pk):
    author = Author.query.get(pk)
    form = UpdateAuthorForm()

    if form.validate_on_submit():
        author.first_name = form.first_name.data
        author.last_name = form.last_name.data
        author.birthdate = form.birthdate.data
        db.session.commit()
        return redirect(url_for('author_list'))

    elif request.method == 'GET':
        form.first_name.data = author.first_name
        form.last_name.data = author.last_name
        form.birthdate.data = author.birthdate

    return render_template('update_author.html', title='Update author', author=author, form=form)


@app.route('/author/delete/<int:pk>', methods=['GET', 'POST'])
def delete_author(pk):
    author = Author.query.get(pk)
    form = DeleteAuthorForm()

    if form.validate_on_submit():
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('author_list'))

    return render_template('delete_author.html', title='Delete  author', author=author, form=form)
