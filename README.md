## Overview

This Flask application displays my family's favorite recipes!  [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) is
used to generate the static files based on the routes specified in the Flask app.  These static files are hosted on
[Netlify](https://www.netlify.com):

![Kennedy Family Recipes](project/static/img/flask_recipe_app_screenshot.png?raw=true "Kennedy Family Recipes")

For details on how this Flask app generates static files, check out the [Generating a Static Site with Flask and Deploying it to Netlify](https://testdriven.io/blog/) blog post on [TestDriven](https://testdriven.io/).

## Website

[https://www.kennedyrecipes.com/](https://www.kennedyrecipes.com/)

## Installation Instructions

Pull down the source code from this GitLab repository:

```sh
git clone git@gitlab.com:patkennedy79/flask-recipe-app.git
```

Create a new virtual environment:

```sh
$ cd flask-recipe-app
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```


## Run the Development Server

In the top-level directory, set the file that contains the Flask application and specify that the development environment should be used:


```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

Navigate to 'http://localhost:5000' to view the website!

## Build the Static Files

In the top-level directory, run the build script:

```sh
(venv) $ python build.py
```

The static files are generated in the */project/build/* directory, which can then be hosted on Netlify.

## Key Python Modules Used

* Flask - micro-framework for web application development
* Jinga - templating engine
* Frozen-Flask - generates static files from Flask routes

This application is written using Python 3.9.0.

## Unit Testing

To run all the tests:

```sh
(venv) $ pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ pytest --cov-report term-missing --cov=project
```
