from models.nguoi_cho_thue import nguoi_cho_thue
import mlab
from mongoengine import *
from customers.customers import customers
mlab.connect()

# tat_ca_nguoi_cho_thue = nguoi_cho_thue.objects()

# nguoi_cho_thue_1 = tat_ca_nguoi_cho_thue[0]

# print(nguoi_cho_thue_1["ten"])

all_customers = customers.objects(gender = 1, contacted = 0)
customers_1 = all_customers[0]
print(customers_1)