from mongoengine import *

class Customers(Document):
    name = StringField()
    gender = IntField()
    yob = IntField()
    email = StringField()
    phone_numb = StringField()
    job = StringField()
    company = StringField()
    contacted = IntField()

