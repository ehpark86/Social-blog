# Social-blog
A Django application that is a combination of Twitter and Medium.

## Functionality
Once a user creates an account, they are able to login.
Users can create posts to different groups.
Users can join different groups.
Users can also follow and unfollow groups of their choosing.


## Running the application

* Using Docker will automatically install all the dependencies in requirements.txt and use Python version 3 required for running this application.

From the root directory /socialblog, run:

```
docker-compose up
```

* Running it manually
Make sure to use Python version 3.

1. Install dependencies from the root directory /socialblog

```
pip3 install -r requirements.txt
```

2. Once you have installed all dependencies, from the root directory /socialblog

```
python manage.py runserver
```
