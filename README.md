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

``` gherkin
source env/bin/activate

export FLASK_APP="run.py"

export SECRET="thisissupposedtobeapassword"

export APP_SETTINGS="development"

export DATABASE_URL="postgresql:username@password    //localhost/dbname"
```

>To activate virtualenv, run:

`source .env`

> or:

`source env/bin/activate`

**Install Dependencies**
> run:

`pip install -r requirements.txt`

> or:

### Test Endpoints
> To test endpoints follow this [link](https://stackoverflow-liter.herokuapp.com/) to the huroku app

> Then use the endpoints below to test them on post man

## API-Endpoints

For user:

Test | API-endpoint |HTTP-Verb | Inputs
------------ | ------------- | ------------ | ------------------
Users can create new question |/api/v1/questions/ | POST | {"question_id":7,"title":"title","body":"body"}
users can view all their questions | /api/v1/questions/ | GET | None
users can view a question | /api/v1/questions/<int:question_id>/ | GET |None
users can modify their question | /api/v1/questions/<int:question_id>/ | PUT |{"title":"title", "body":"body"}
users can delete a question | /api/v1/questions/<int:question_id>/ | DELETE |None
users can view all answers to a question | /api/v1/answers/<int:question_id> | GET | None
Users can create a new answer |/api/v1/answers/<int:question_id>/ | POST |{"question_id":1,"answer_id":7,"body":"body"}
users can view an answer | /api/v1/answers/<int:question_id>/<int:answer_id> | GET |None 
users can modify their answers | /api/v1/answers/<int:question_id>/<int:answer_id> | PUT |{"body":"body"}
users can delete an answer | /api/v1/answers/<int:question_id>/<int:answer_id> | DELETE | None

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

*Bootcamp-cohort31-comrades*

*Rockstars-Team*

### Support or Contact

[Github Pages](https://lawrencechege.github.io/StackOverflow-lite/)

[Heroku App](https://stackoverflow-liter.herokuapp.com/)

*"If you know, You know"*