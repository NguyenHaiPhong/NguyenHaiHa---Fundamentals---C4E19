from mongoengine import *
from datetime import datetime 

class Customers(Document):
    name = StringField()
    gender = IntField()
    yob = IntField()
    email = EmailField()
    phone_numb  = StringField()
    job = StringField()
    company = StringField() 
    contacted = BooleanField()

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

class Users(Document):
    full_name = StringField()
    email = EmailField(required=True)
    log_in = StringField(required=True)
    password = StringField(required=True)
    is_admin = BooleanField(default=False)

class Orders(Document):
    model_id = ReferenceField(Models)
    user_id = ReferenceField(Users)
    order_time = DateTimeField(default=datetime.now())
    is_accecpted = BooleanField(default=False)