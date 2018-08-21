""" holds resources for the app """
import datetime
QUESTIONS_DICT = [
    {
        "question_id": 1,
        "user_id": 1,
        "title": "hey?",
        "body": "how are you doing?",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
    },
    {
        "question_id": 2,
        "user_id": 1,
        "title": "work done?",
        "body": "have you completed the project?",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
    },
    {
        "question_id": 3,
        "user_id": 2,
        "title": "hey mum",
        "body": "anything i can get you from the mall?",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
    },
    {
        "question_id": 4,
        "user_id": 2,
        "title": "groceries",
        "body": "do we have enough groceries for the week?",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
    }
]
ANSWERS_DICT = [
    {
        "answer_id": 1,
        "user_id": 3,
        "question_id": 1,
        "body": "hello, am doing great",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
        "status": "Pending"
    },
    {
        "answer_id": 2,
        "user_id": 3,
        "question_id": 2,
        "body": "yea, am done just a few things to polish",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
        "status": "Pending"
    },
    {
        "answer_id": 3,
        "user_id": 4,
        "question_id": 1,
        "body": "hey, am good here",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
        "status": "Pending"
    },
    {
        "answer_id": 4,
        "user_id": 5,
        "question_id": 3,
        "body": "hey son, i dont know ,lemme check",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
        "status": "Pending"
    },
    {
        "answer_id": 5,
        "user_id": 5,
        "question_id": 4,
        "body": "yes you can buy groceries",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
        "status": "Pending"
    },
    {
        "answer_id": 6,
        "user_id": 5,
        "question_id": 4,
        "body": "and also buy some milk",
        "date_created": str(datetime.datetime.now()),
        "date_modified": str(datetime.datetime.now()),
        "upvotes": 3,
        "downvotes": 1,
        "answers": 0,
        "status": "Pending"
    }
]
