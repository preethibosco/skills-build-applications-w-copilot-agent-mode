from mongoengine import Document, StringField, EmailField, ListField, IntField, DateField

class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(max_length=255, required=True)

class Team(Document):
    name = StringField(max_length=255, required=True)
    members = ListField(StringField())

class Activity(Document):
    user_id = StringField(required=True)
    type = StringField(max_length=255, required=True)
    duration = IntField(required=True)
    date = DateField(required=True)

class Leaderboard(Document):
    user_id = StringField(required=True)
    score = IntField(required=True)

class Workout(Document):
    name = StringField(max_length=255, required=True)
    description = StringField()
    duration = IntField(required=True)
