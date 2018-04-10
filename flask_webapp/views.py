"""Class based views for the webapp."""
import flask
from flask.views import MethodView
from werkzeug import secure_filename
from flask_webapp import forms
from flask_webapp import ocr
import os


class IndexView(MethodView):
    """The home  page view."""

    def get_template_name(self):
        """Return a string containing the name of this view's template."""
        return 'index.html'

    def get_context(self, request, **kwargs):
        """Process data given in the request."""
        # instantiate the form. It gets what it needs from flask.request
        form = forms.UploadForm()
        # generate initial context
        context = dict(form=form)
        # over write context with any keyword arguments
        context.update(**kwargs)
        return context

    def get(self, **kwargs):
        """Handle get requests."""
        context = self.get_context(flask.request, **kwargs)
        context.update(**kwargs)
        return flask.render_template(self.get_template_name(), context=context)

    def post(self, **kwargs):
        form = forms.UploadForm()
        if form.validate_on_submit():
            uniqueID = 192385791287519
            file = flask.request.files[form.file.name]
            name = uniqueID + secure_filename(file.filename)
            old_path = os.path.join(os.path.dirname(__file__), 'uploads', name)
            # TODO: save image file
            file.save(old_path)
            # TODO: get OCR output from saved image file
            ocr.ocr_file(old_path)
            # TODO: process ocr output to extract serial number
            # TODO: rename the saved file to include the extracted serial number and the date

            return self.get(successful_upload=True, data=file)
        return self.get(successful_upload=False)
