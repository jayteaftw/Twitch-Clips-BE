from flask import Blueprint, render_template, request, flash, redirect, url_for
from db_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth_api = Blueprint('auth_api', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth_api.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("index.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_api.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('Email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        #password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth_api.tag_select'))

    return render_template("index.html", user=current_user)



@auth.route('/sign-up/tag-select', methods=['GET', 'POST'])
def tag_select():
    if request.method == 'Post':
        tags = request.form.get('tags')

        if len(tags) < 1:
            flash('Please select atleast 1 tag', category='error')
        else:
            new_user_tag = Tag(tags=tags)
            db.session.add(new_user_tag)
            db.session.commit() 
            login_user(new_user_tag, remember = True)
            flash('User tags selected!', category='success')
            return redirect(url_for('auth_api.home'))


"""
class auth_API(Resource):

    def post():
        pass
    
    #Finds new user in DB
    def get():
        pass

    def delete():
        pass

    def patch():
        pass

"""