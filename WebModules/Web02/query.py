from models.nguoi_cho_thue import nguoi_cho_thue
import mlab
from mongoengine import *
from customers.customers import customers
mlab.connect()

# tat_ca_nguoi_cho_thue = nguoi_cho_thue.objects()

# nguoi_cho_thue_1 = tat_ca_nguoi_cho_thue[0]

# print(nguoi_cho_thue_1["ten"])

# all_customers = customers.objects(gender = 1, contacted = 0)
# customers_1 = all_customers[0]
# print(customers_1)
id_to_find = "5b5ec393fd2b0f2a98faaf8b"
find_customer_2 = customers.objects.with_id(id_to_find)
# print(find_customer_2.to_mongo())
# print(find_customer_2)

# if find_customer_2 is not None:
#     find_customer_2.delete()
#     print("Delete.")
# else:
#     print("Not found.")

print("Before:", find_customer_2.to_mongo())
find_customer_2.update(set__name = "Numb", set__yob = 2009)
find_customer_2.reload()
print("After:", find_customer_2.to_mongo())