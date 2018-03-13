"""Class based forms that automatically handle validation."""
import flask_wtf
from flask_wtf.file import FileField, FileRequired


class UploadForm(flask_wtf.FlaskForm):
    file = FileField('Image File', validators=[FileRequired()])