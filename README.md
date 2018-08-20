## Welcome to Stackoverflow lite
[![codecov](https://codecov.io/gh/lawrenceChege/StackOverflow-lite/branch/challenge-2/graph/badge.svg)](https://codecov.io/gh/lawrenceChege/StackOverflow-lite)

[![Build Status](https://travis-ci.org/lawrenceChege/StackOverflow-lite.svg?branch=159869319-challenge-2--updated)](https://travis-ci.org/lawrenceChege/StackOverflow-lite)

## what it does

It provides the API endpoints for [Stackoverflow lite](https://stackoverflow-liter.herokuapp.com/)
> an app that allows users to ask questions, get answers and give answers to other user's question.

## Usage

* As a User, you can:
                    * Create an account
                    * Log in into the account
                    * Create a question
                    * View all your questions
                    * View a specific question
                    * View a specific answer to a question
                    * View the status of a request
                    * Modify a question
                    * delete a question
                    * answer a question
                    * modify an answer
                    * delete an answer
                    * view all answers
                    * view all answers to a question


## Prerequisites

* Python 3.6 or later
* Git
* Virtualenv

## Installation

### Download option

* Go to [Stackoverflow lite](https://github.com/lawrenceChege/StackOverflow-lite) on github
* Download the zip file and extract it
* Right click on the folder and open with terminal on linux or bash

>> we will continue from there :-)

** Cloning option **

* On your favorite terminal
* cd to where you want the repo to go
* Run the following command:

`git clone https://github.com/lawrenceChege/StackOverflow-lite.git`

* Then:

`cd Stackoveflow-lite`

## Virtual environment

> Now create a vitual environment, run:

`virtualenv env`

> or :

`python3 -m venv env`

> or any other that you know of.
> > Create a .env file and configure it with:

``` source env/bin/activate

export FLASK_APP="run.py"

export SECRET="thisissupposedtobeapassword"

export APP_SETTINGS="development"

export DATABASE_URL="postgresql:username@password    //localhost/Pro-Tracker" ```

>To activate virtualenv, run:

`source .env`

> or:

`source env/bin/activate`

**Install Dependencies**
> run:

`pip install -r requirements.txt`

> or:

`python3 -m pip install -r requirements.txt`

## API-Endpoints

For user:

Test | API-endpoint |HTTP-Verb
------------ | ------------- | ------------
Users can create new question |/api/v1/questions/ | POST
users can view all their questions | /api/v1/questions/ | GET
users can view a question | /api/v1/questions/<question_id>/ | GET
users can modify their question | /api/v1/questions/<question_id>/ | PUT
users can delete a question | /api/v1/questions/<question_id>/ | DELETE
Users can create a new answer |/api/v1/answers/<int:question_id>/ | POST
users can view all answers to aquestion | /api/v1/answers/<question_id> | GET
users can view an answer | /api/v1/answers/<question_id>/<answer_id> | GET
users can modify their answers | /api/v1/answers/<question_id>/<answer_id> | PUT
users can delete an answer | /api/v1/answers/<question_id>/<answer_id> | DELETE

*Testing*
> you could test each endpoint on postman or curl
> you could also run
`nosetests`
or
`pytest`

*this readme will be updated periodically*
### Author

*Lawrence Chege*

### Acknowledgement

*Andela Kenya*
*Rockstars-Team*

### Support or Contact


