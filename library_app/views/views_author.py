""" Views file for author model in library_app """
# pylint: disable=invalid-name, cyclic-import

from flask import request, render_template, redirect, url_for

from library_app import db, app
from library_app.forms import CreateAuthorForm, UpdateAuthorForm, DeleteAuthorForm
from library_app.models.author import Author


@app.route('/author/list')
def author_list():
    """ List of authors page """
    authors = Author.query.all()

    return render_template('list_author.html', title='List of authors', authors=authors)


@app.route('/author/detail/<int:pk>')
def detail_author(pk):
    """ Author detail page """
    author = Author.query.filter_by(id=pk).first()

    if author is None:
        return render_template('index.html', title='Page not found', content='404 error')

    return render_template('detail_author.html', title='Author detail', author=author)


@app.route('/author/create', methods=['GET', 'POST'])
def create_author():
    """ Create author page """
    form = CreateAuthorForm()

    if form.validate_on_submit():
        author = Author(first_name=form.first_name.data, last_name=form.last_name.data, birthdate=form.birthdate.data)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('author_list'))

    return render_template('create_author.html', title='Create new author', form=form)


@app.route('/author/update/<int:pk>', methods=['GET', 'POST'])
def update_author(pk):
    """ Update author page """
    author = Author.query.get(pk)
    form = UpdateAuthorForm()

    if form.validate_on_submit():
        author.first_name = form.first_name.data
        author.last_name = form.last_name.data
        author.birthdate = form.birthdate.data
        db.session.commit()
        return redirect(url_for('author_list'))

    if request.method == 'GET':
        form.first_name.data = author.first_name
        form.last_name.data = author.last_name
        form.birthdate.data = author.birthdate

    return render_template('update_author.html', title='Update author', author=author, form=form)


@app.route('/author/delete/<int:pk>', methods=['GET', 'POST'])
def delete_author(pk):
    """ Delete author page """
    author = Author.query.get(pk)
    form = DeleteAuthorForm()

    if form.validate_on_submit():
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('author_list'))

    return render_template('delete_author.html', title='Delete  author', author=author, form=form)
