from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

database = client.get_default_database()

customers = database["customers"]
get_all_customers = customers.find()
count_all_customers_group_by_ref = 0

for all_customers in get_all_customers:
    for key in all_customers.keys():
        if key == "ref":
            count_all_customers_group_by_ref += 1
print("Number of customers group by 'ref':", count_all_customers_group_by_ref)




