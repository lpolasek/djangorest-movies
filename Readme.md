djangorest-movies
=================
Simple movies django REST application.

Requirements:
-------------
* Python 3.8

Installation:
-------------
* clone Git repo

        git clone https://github.com/lpolasek/djangorest-movies.git

* satisfy dependencies

        cd djangorest-movies
        python3 -m venv env
        source env/bin/activate
        pip install -r deploy/requirements.txt
        ./manage.py migrate
        ./manage.py createsuperuser --email admin@example.com --username admin

* test djangorest-movies

        ./manage.py runserver

    - open [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) in a web browser


Available endpoints:
--------------------

You can access the list of available endoints (only when DEBUG = True) here:

  [http://127.0.0.1:8000/swagger-ui/](http://127.0.0.1:8000/swagger-ui/)

Notice that some endpoints are only available when you have loged in into the system.

Live Demo:
----------

You can also try a live demo running at [http://movies.polasoft.com.ar/api/](http://movies.polasoft.com.ar/api/).

Notes:
------

* I have decided to use [swagger-ui](https://swagger.io/tools/swagger-ui/) as an end-point documenter, because of its clean UI. The other options have a more complex UI.

* To simplify the model, I chose to store the aliases list as a tokenized string, for doing that I had to subclassify *serializers.ListField* because the serializers schemas are hardcoded in *rest_framework/schemas/openapi.py*.
