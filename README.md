# Twitter
```
Making a twitter like app
```
OS: ubuntu0.18.04.1
Database used: PostgreSQL 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
Framework: Django 2.2.7
Language: Python 3.6.8
IDE: Visual Studio Code
Other packages used:
    djangorestframework==3.10.3
    pkg-resources==0.0.0
    psycopg2==2.8.4
    pytz==2019.3
    sqlparse==0.3.0

There are two models : User and Tweet

Class Diagram: Tweet has a User

User has the following attributes: Email and Name
Email  is th email id of the user and is unique (not a primary key)
Name is the name of the user

Tweet has the following attributes: user, text, date_time_created, date_time_updated and delete_tweet
user is a foreign key to the class User
text is your tweet text with max length 140 characters
date_time_created is the date-time of the creation of your tweet and remains constant
date_time_updated is the date-time you last edited your tweet and can change
delete_tweet is a flag to do soft delete of a tweet later
Tweet also has a short_text function that returns the first 10 characters of your tweet text followed by 3 fullstops

Serializers are created : UserSerializer, TweetSerializer, TweetDeleteSerializer
User and Tweet model data are serialized and deserialized. In TweetSerializer everything except delete_tweet is accessible and in TweetDeleteSerializer, only delete_tweet is accessible. So TweetDeleteSerializer is specifically built for the soft-delete function

In views.py we have the different api views which are later on passed to the urls for easy access. 

Front end also created with HTML, CSS, ReactJS
