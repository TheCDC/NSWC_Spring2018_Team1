import flask
from . import views
import random
app = flask.Flask(__name__)
# necessary for CSRF
app.config['SECRET_KEY'] = str(int(random.random() * 100000000000))

app.add_url_rule('/', view_func=views.IndexView.as_view('index'))

if __name__ == '__main__':
    app.run(debug=True)