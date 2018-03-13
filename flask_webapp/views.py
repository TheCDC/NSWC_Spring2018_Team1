"""Class based views for the webapp."""
import flask
from flask.views import MethodView
from . import forms


class IndexView(MethodView):
    """The home  page."""

    def get_template_name(self):
        return 'index.html'

    def get_context(self, request, **kwargs):
        """Process data given in the request."""
        form = forms.UploadForm()
        context = dict(
            form=form, success=request.args.get('successful_upload'))
        context.update(**kwargs)
        return context

    def get(self, **kwargs):
        """Handle get requests."""
        return flask.render_template(
            self.get_template_name(),
            context=self.get_context(flask.request, **kwargs))


class UploadView(MethodView):
    def post(self, **kwargs):
        form = forms.UploadForm()
        if form.validate_on_submit():
            return flask.redirect(
                flask.url_for('index', successful_upload=True))
        return flask.redirect(flask.url_for('index', successful_upload=False))
