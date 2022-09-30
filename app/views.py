from flask import render_template, request, redirect, url_for, flash

from app import app, db
from .forms import UserForm
from .forms import UpdateUserForm
from .forms import DeleteUserForm
from .models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html', name="Starter Template CRUD App using Flask and SQLite")


@app.route('/users')
def show_users():
    # or users = User.query.all()
    users = db.session.query(User).all()
    return render_template('show_users.html', users=users)


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    user_form = UserForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Get validated data from form
            # You could also have used request.form['name']
            name = user_form.name.data
            # You could also have used request.form['email']
            email = user_form.email.data

            # save user to database
            user = User(name, email)
            db.session.add(user)
            db.session.commit()

            flash('User successfully added.')
            return redirect(url_for('show_users'))

    flash_errors(user_form)
    return render_template('add_user.html', form=user_form)


@app.route('/update-user', methods=['GET', 'POST', 'PUT'])
def update_user():
    update_user_form = UpdateUserForm()

    if request.method == 'POST' or request.method == 'PUT':
        if update_user_form.validate_on_submit():
            # Get validated data from form
            # You could also have used request.form['id']
            id = update_user_form.id.data
            # You could also have used request.form['name']
            updated_name = update_user_form.name.data
            # You could also have used request.form['email']
            updated_email = update_user_form.email.data

            # update user from database
            user = db.session.query(User).filter(User.id == id).first()
            user.name = updated_name
            user.email = updated_email
            db.session.commit()

            flash('User successfully updated.')
            return redirect(url_for('show_users'))

    flash_errors(update_user_form)
    return render_template('update_user.html', form=update_user_form)


@app.route('/delete-user', methods=['GET', 'POST'])
def delete_user():
    delete_user_form = DeleteUserForm()

    if request.method == 'POST':
        if delete_user_form.validate_on_submit():
            # Get validated data from form
            # You could also have used request.form['email']
            email = delete_user_form.email.data

            # delete user from database
            user = db.session.query(User).filter(User.email == email).first()
            db.session.delete(user)
            db.session.commit()

            flash('User successfully deleted.')
            return redirect(url_for('show_users'))

    flash_errors(delete_user_form)
    return render_template('delete_user.html', form=delete_user_form)

# Flash errors from the form if validation fails


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
