from models.nguoi_cho_thue import nguoi_cho_thue
from customers.customers import customers
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()
# print(fake.name())
# print(fake.address())
# for i in range(20):
#     print("Saving", i + 1, "...")
#     nguoi_cho_thue_moi = nguoi_cho_thue(
#         ten = fake.name(),
#         nam_sinh = randint(1990, 2000),
#         gtinh = randint(0, 1),
#         chieu_cao = randint(150, 200),
#         so_dt = fake.phone_number(),
#         dia_chi = fake.address(),
#         tinh_trang = choice([True, False])
#     )
#     nguoi_cho_thue_moi.save()

for i in range(30):
    print("saving", i + 1, "...")
    new_customer = customers(
        name = fake.name(),
        gender = randint(0, 1),
        yob = randint(1990, 2000),
        email = fake.email(),
        phone_numb = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = randint(0 ,1)
    )
    new_customer.save()