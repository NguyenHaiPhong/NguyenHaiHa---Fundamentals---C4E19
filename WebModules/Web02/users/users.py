from mongoengine import *

class Users(Document):
    full_name = StringField()
    email = StringField()
    sign_in = StringField()
    password = StringField()