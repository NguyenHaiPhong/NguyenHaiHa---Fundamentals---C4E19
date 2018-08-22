from classes.classes import *
import mlab
from faker import Faker as fake
from random import randint, choice, sample
from random_list import image_list_link, description_list
mlab.connect()

new_admin = Users(
    full_name = "ha",
    email = "ha",
    log_in = "ha",
    password = "ha",
    is_admin = True
)
new_admin.save()

new_user = Users(
    full_name = "ha",
    email = "ha",
    log_in = "ha",
    password = "ha"
)
new_user.save()