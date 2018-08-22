from classes.classes import *
import mlab
mlab.connect()

# all_customers = Customers.objects(gender = 1)
# a = len(all_customers)
# if a != 0:
#     print("haha")
# elif a == 0:
#     print("huhu")
all_orders = Orders.objects(is_accecpted = False)
        # for order in all_orders:
print(all_orders[0].to_mongo())
a = all_orders[0].model_id
# print(a)
# print(type(a))
# b = a["name"]
# print(b)
# print(type(b))
# model_name = all_orders[0]["name"]
# user = Users.objects.with_id(str(user_id))
# print(user[0].to_mongo())

# print(a)
# print(type(a))
# b = all_customers[0]
# print(b.to_mongo())
# a = all_customers[0].id
# print(a)
# print(type(a))

# session = {}
# session["customer_logged_in"] = a
# print(session)
# b = session["customer_logged_in"]
# print(b)
# print(type(b))

# a = all_customers[0].id
# print(a)
# customers_1 = all_customers[0]
# a = customers_1
# a = customers_1[0]
# print(a)
# print(customers_1.to_mongo())
# print(type(customers_1))
# id_to_find = "5b6ab4a9fd2b0f2d482edbaa"
# find_customer = Customers.objects(gender = 1)
# print(find_customer_2.to_mongo())
# print(find_customer)
# for customer in find_customer:
    # print(customer)
# if find_customer_2 is not None:
#     find_customer_2.delete()
#     print("Delete.")
# else:
#     print("Not found.")

# print("Before:", find_customer_2.to_mongo())
# print(type(find_customer_2))
# find_customer_2.update(set__name = "Numb", set__yob = 2009)
# find_customer_2.reload()
# print("After:", find_customer_2.to_mongo())
# haha = ([('_id', ('5b6ab4a9fd2b0f2d482edbaa')), 
# ('name', 'Malik Kim'), ('gender', 1), ('yob', 1991), 
# ('email', 'xsmith@hotmail.com'), 
# ('phone_numb', '(534)452-4789x4316'), 
# ('job', 'Chief Marketing Officer'), 
# ('company', 'Patrick, Pitts and Anderson'), 
# ('contacted', 1)])
# a = haha[0][1]
# print(a)