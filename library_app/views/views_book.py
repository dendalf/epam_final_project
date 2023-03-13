""" Views file for book model in library_app """
# pylint: disable=invalid-name, cyclic-import
from datetime import datetime

from flask import request, render_template, redirect, url_for

from library_app import db, app
from library_app.forms import CreateBookForm, FilterBookForm
from library_app.forms import DeleteBookForm
from library_app.forms import UpdateBookForm
from library_app.models.author import Author
from library_app.models.book import Book


@app.route('/book/list')
def read_books():
    """ List of books page """
    form = FilterBookForm()
    if request.args.get('date_published_start') and request.args.get('date_published_end'):
        form.date_published_start.data = datetime.strptime(request.args.get('date_published_start'), '%Y-%m-%d')
        form.date_published_end.data = datetime.strptime(request.args.get('date_published_end'), '%Y-%m-%d')
        books = Book.query.filter((request.args.get('date_published_start') <= Book.date_published) & (Book.date_published <= request.args.get('date_published_end'))).all()
    else:
        books = Book.query.all()

    return render_template('list.html', title='List of books', books=books, form=form)


@app.route('/book/detail/<int:pk>')
def detail(pk):
    """ Book detail page """
    book = Book.query.filter_by(id=pk).first()

    if book is None:
        return render_template('index.html', title='Page not found', content='404 error')

    return render_template('detail.html', title='Book detail', book=book)


@app.route('/book/create', methods=['GET', 'POST'])
def create_book():
    """ Create Book page """
    form = CreateBookForm()
    form.author.choices = [("", "-----")] + [(author.id, author) for author in Author.query.all()]

    if form.validate_on_submit():
        book = Book(title=form.title.data, author_id=form.author.data, date_published=form.date_published.data, price=form.price.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('read_books'))

    return render_template('create.html', title='Create new book', form=form)


@app.route('/book/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    """ Update Book page """
    book = Book.query.get(pk)
    form = UpdateBookForm()
    form.author.choices = [(author.id, author) for author in Author.query.all()]

    if form.validate_on_submit():
        book.title = form.title.data
        book.author_id = form.author.data
        book.date_published = form.date_published.data
        book.price = form.price.data
        db.session.commit()
        return redirect(url_for('read_books'))

    if request.method == 'GET':
        form.author.default = book.author_id
        form.process()
        form.title.data = book.title
        form.date_published.data = book.date_published
        form.price.data = book.price

    return render_template('update.html', title='Update book', book=book, form=form)


@app.route('/book/delete/<int:pk>', methods=['GET', 'POST'])
def delete(pk):
    """ Delete Book page """
    book = Book.query.get(pk)
    form = DeleteBookForm()

    if form.validate_on_submit():
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('read_books'))

    return render_template('delete.html', title='Delete  book', book=book, form=form)

