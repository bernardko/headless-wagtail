# headless-wagtail - A GraphQL Headless CMS built with Wagtail

This repository holds the source code for [ketonetic.com](https://ketonetic.com) headless CMS. This is my experiment in building a headless CMS using Wagtail to serve GraphQL. [Ketonotic](https://github.com/bernardko/ketonetic) is built with GatsbyJS which is used to generate a static website. 

## Features
 - Built with Django Framework and Wagtail CMS.
 - GraphQL implemented using wagtail-graphql app.
 - GraphQL serves Wagtail Pages built with StreamField and Images.
 - django-configurations for settings handling between environments.
 
## Requirements and Usage
  1. Python 3.7.13
  2. Pipenv for package management
  3. Django 2.2.3

Make sure you have pipenv installed:
```
pip install pipenv
```

Clone the repository, install the requirements and fill out the .env.example for your environment variables:
```
git clone https://github.com/bernardko/headless-wagtail/
cd headless-wagtail
pipenv install
cp .env.example .env
```

Activate pipenv shell to load environment variables and run the dev server to start developing:
```
pipenv shell
python manage.py runserver
```
