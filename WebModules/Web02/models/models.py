from mongoengine import *

class Models(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone_numb = StringField()
    address = StringField()
    avatar = StringField()
    description = ListField()
    measurements = ListField()
    status = IntField()


