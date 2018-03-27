"""Class based views for the webapp."""
import flask
from flask.views import MethodView
from . import forms


class IndexView(MethodView):
    """The home  page view."""

    def get_template_name(self):
        """Return a string containing the name of this view's template."""
        return 'index.html'

    def get_context(self, request, **kwargs):
        """Process data given in the request."""
        form = forms.UploadForm()
        context = dict(form=form)
        # over write context with any keyword arguments
        context.update(**kwargs)
        return context

    def get(self, **kwargs):
        """Handle get requests."""
        # generate initial context
        context = self.get_context(flask.request, **kwargs)
        context.update(**kwargs)
        return flask.render_template(self.get_template_name(), context=context)

    def post(self, **kwargs):
        form = forms.UploadForm()
        if form.validate_on_submit():
            file = flask.request.files[form.file.name]
            return self.get(successful_upload=True, data=file)
        return self.get(successful_upload=False)
