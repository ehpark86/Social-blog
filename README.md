# Social-blog
A Django application that is a combination of Twitter and Medium.

## Running the application

* Using Docker will automatically install all the dependencies in requirements.txt and use Python version 3 required for running this application.

From the root directory /socialblog, run:

'''bash
docker-compose up
'''

* Running it manually
Make sure to use Python version 3.

1. Install dependencies from the root directory /socialblog

'''bash
pip3 install -r requirements.txt
'''

2. Once you have installed all dependencies, from the root directory /socialblog

'''bash
python manage.py runserver
'''

