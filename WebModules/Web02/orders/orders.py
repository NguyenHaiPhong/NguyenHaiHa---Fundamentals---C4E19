from mongoengine import *
from users.users import Users
from models.models import Models
from datetime import datetime

class Orders(Document):
    model_id = ReferenceField(Models)
    user_id = ReferenceField(Users)
    order_time = DateTimeField(default=datetime.now())
    is_accecpted = BooleanField(default=False)