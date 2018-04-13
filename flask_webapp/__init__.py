import flask
from flask_webapp import views
import random
import os

SECRET_KEY = os.environ.get('SECRET_KEY', str(
    int(random.random() * 100000000000)))
app = flask.Flask(__name__)
# necessary for CSRF token.
app.config['SECRET_KEY'] = SECRET_KEY

app.add_url_rule(
    '/',  # the url endpoint
    view_func=views.IndexView.as_view(
        'index')  # a meaningful name for the endpoint
)

if __name__ == '__main__':
    app.run(debug=True)
