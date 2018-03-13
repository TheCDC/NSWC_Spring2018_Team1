import flask

from flask.views import View, MethodView


class IndexView(MethodView):
    def get_template_name(self):
        return 'index.html'

    def get(self, **kwargs):
        return flask.render_template(self.get_template_name())