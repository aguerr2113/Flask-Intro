# first import Flask class(an instance of this class wil be our WSGI app)
from flask import Flask, url_for, request
from markupsafe import escape

# Second we create an instance of this class
app = Flask(__name__)

# Third we use rout() decoratro to tell flask what url should trigger our function
@app.route('/hello')
# the function returns the message we want to display in the user browser the default  content type is HTML, so HTML in the string will be rendered by the browser
def hello_world():
    return "<h1> Hello Worl</h1>"

@app.route('/')
def index():
    return 'index page'

# Variable Rules/URLBUILDING
@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile for that user
    return f'User {escape(username)}.'

# URL BUILDIG
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile' username='JohnDoe'))

# UNIQUE URLS/REDIRECTION BEHAVIOR

@app.route('/projects/')
def projects():
    return 'the project page'
# the canonical RL for the proejct endpoint has a trainling slash. if you access it without the trailing slahs ,Flask redirects yo uto the canonical URL with thte trailing slash

@app.route('/about')
def about():
    return'the about page'
# the cononical URL for the about endopint does not have a trainling slashaccessing the url with a trailing slash produces a 404

# HTTP Methods
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    