"""Class based views for the webapp."""
import datetime

import flask
from flask.views import MethodView
from werkzeug import secure_filename
from flask_webapp import forms
from flask_webapp import ocr
import os


class IndexView(MethodView):
    """The home  page view."""

    count = 1

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
            uniqueID = IndexView.count
            IndexView.count += 1
            file = flask.request.files[form.file.name]
            name = uniqueID.__str__() + secure_filename(file.filename)
            old_path = os.path.join(os.path.dirname(__file__), 'uploads', name)
            # save image to file
            file.save(old_path)
            # get OCR output from saved image file
            output = ocr.ocr_file(old_path)
            # process ocr output to extract serial number
            serialNumber = ocr.filter_serial(output)
            if not serialNumber:
                serialNumber = 'NOSERIAL'

            # rename the saved file to include the extracted serial number and
            # the date
            newname = str(serialNumber) + ' ' + \
                str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
            newpath = os.path.join(
                os.path.dirname(__file__), 'uploads', newname)
            os.rename(old_path, newpath)

            return self.get(successful_upload=True, data=file, serial_number=serialNumber, ocr_output=output)
        return self.get(successful_upload=False)
