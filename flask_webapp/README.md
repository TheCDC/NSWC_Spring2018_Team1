# Flask webapp

`__init__.py` contains the app itself and its configuration.

`forms.py` contains web form class definitions that handle input validation

`views.py` contains view classes that actually define the behavior of url endpoints.

`templates/` contains html templates designed for the jinaj2 templating engine.

# Getting started

`pipenv shell` will oad you into the virtual environment.

`flask run` will start the server for the web app. The `flask` command is provided by the flask python package. The `.env` file contains the environment variables necessary for the `flask` command.

# Adding endpoints

The workflo for adding an endpoint goes like this:

 - Create the view class in views.py and defined the necessary get/post methods. The classes don't technically need any other methods.
 - Add the url rule to the in `__init__.py`