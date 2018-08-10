from mongoengine import *

class Admins(Document):
    full_name = StringField()
    email = StringField()
    log_in = StringField()
    password = StringField()
