BRAWL RESULT SUBMISSION

web app version of game result submission form.  This requires python and django to run.

INSTALLATION

1. Make sure you have python installed on your machine - https://www.python.org/downloads/
2. Python usually installs pip.  Install django with pip `pip install django` (you may want to do this in a virtual environment - https://docs.python.org/3/library/venv.html)

USAGE

1. Make sure there is a credentials.json file in the root folder of the project.  You must also make sure that you're google account has been added as a test user in order to properly authorize access.
2. From the top level brawl folder with `manage.py` run `python manage.py runserver` this will start the django development server
3. Navigate to 127.0.0.1:8000/results on the browser of your choice
