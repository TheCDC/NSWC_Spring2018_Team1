import flask
import views

app = flask.Flask(__name__)

app.add_url_rule('/', view_func=views.IndexView.as_view('index'))

if __name__ == '__main__':
	app.run(debug=True)