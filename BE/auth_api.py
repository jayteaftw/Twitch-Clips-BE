from flask import request, render_template, Blueprint
from flask_restful import Api, Resource, reqparse

auth_post_args = reqparse.RequestParser()
auth_post_args.add_argument("email",    help="oAuth key for clinician access",            required=True)
auth_post_args.add_argument("password",   help="oAuth key's date in ObjectID form",         required=True)

auth_get_args = reqparse.RequestParser()
auth_get_args.add_argument("email",    help="oAuth key for clinician access",            required=True)
auth_get_args.add_argument("password",   help="oAuth key's date in ObjectID form",         required=True)


class auth_API(Resource):

    def get(self):
        args = auth_post_args.parse_args()
        email = args["email"]
        password = args["password"]
        print(email, password)
        return {"email": email, "password": password}, 200
    
    def post(self):
        language = request.args.get('language')
        password = request.args.get("password")
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            print("here")
            json = request.json
            print("here")
            print(json)
        print(password)
        print(language)
        return {"hello":"yes"}, 200
    
    def delete(self):
        pass

    def patch(self):
        pass

example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/signIn', methods=['GET', 'POST'])
def signIn():
    print(request)
    args = request.json
    print(args)
    return {"token": "00000000", "email":args["email"]}, 200


@example_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        print(request)
        args = request.json
        print(args)
        data = "https://clips.twitch.tv/embed?clip=IcySparklyPieBCWarrior-uc8jRlxGER684i-2, https://clips.twitch.tv/embed?clip=IgnorantSourBulgogiKappa-aOypuRSQhb1da0MW, https://clips.twitch.tv/embed?clip=StormyTentativeGooseNerfBlueBlaster-fz6AoxMLgYa1bK4K, https://clips.twitch.tv/embed?clip=SingleDrabTigerKAPOW-psNF6qOiQWIFMvC9"
        return {"links":data}, 200
    


@example_blueprint.route('/querytwo', methods=['GET', 'POST'])
def querytwo():
    args = request.json
    print("links")
    data = "https://clips.twitch.tv/embed?clip=IcySparklyPieBCWarrior-uc8jRlxGER684i-2, https://clips.twitch.tv/embed?clip=IgnorantSourBulgogiKappa-aOypuRSQhb1da0MW, https://clips.twitch.tv/embed?clip=StormyTentativeGooseNerfBlueBlaster-fz6AoxMLgYa1bK4K, https://clips.twitch.tv/embed?clip=SingleDrabTigerKAPOW-psNF6qOiQWIFMvC9"
    return {"links":data}, 200





""" auth_API = Blueprint('auth_api', __name__)


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
            return redirect(url_for('auth_api.home')) """




