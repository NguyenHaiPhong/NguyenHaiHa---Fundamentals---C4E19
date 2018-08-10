from models.models import Models
from customers.customers import Customers
from admins.admins import Admins
from users.users import Users   
import mlab
from faker import Faker 
from random import randint, choice, sample
from random_list import image_list_link, description_list

mlab.connect()

fake = Faker()

# for key, value in enumerate(image_list_link):
#     print("Saving", key + 1, "...")
#     new_model = Models(
#         name = fake.name(),
#         yob = randint(1990, 2000),
#         gender = randint(0, 1),
#         height = randint(150, 200),
#         phone_numb = fake.phone_number(),
#         address = fake.address(),
#         avatar = value,
#         description = sample(description_list, 6),
#         measurements = [randint(70,90), randint(60, 70), randint(70,100)],
#         status = randint(0, 1)
#     )
#     new_model.save()

# for i in range(30):
#     print("saving", i + 1, "...")
#     new_customer = Customers(
#         name = fake.name(),
#         gender = randint(0, 1),
#         yob = randint(1990, 2000),
#         email = fake.email(),
#         phone_numb = fake.phone_number(),
#         job = fake.job(),
#         company = fake.company(),
#         contacted = randint(0 ,1)
#     )
#     new_customer.save()

# new_admin = Admins(
#     full_name = "ha",
#     email = "ha",
#     log_in = "ha",
#     password = "ha"
# )
# new_admin.save()

new_user = Users(
    full_name = "ha",
    email = "ha",
    sign_in = "ha",
    password = "ha",
)
new_user.save()