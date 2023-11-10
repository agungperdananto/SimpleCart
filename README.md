# SimpleCart
implement simple cart and promotion

# Setup Guide


## Install, create and activate virtualenv

## Install requirements

    pip install -r requirements.txt
## set env variable
create new database, in this case we're using postgresql

## set env variable

create file .env in the root of the folder, and fill with you credential of your database

      
    DB_USER = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DB_PORT = ""
    DB_NAME = ""
    FLASK_DEBUG = true

## Create table

run `flask create`to create tables from models.

## Run the app
to run the web app simply  use

    flask run

to access swagger use url `localhost:5000/apidocs`


## Debt

 - Cart Update
 - Same product validation on cart
 - Unit test
 - Unit test coverage
 - CI setup 
