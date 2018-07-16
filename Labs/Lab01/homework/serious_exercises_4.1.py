from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

database = client.get_default_database()
customers = database["customers"]
get_all_customers = customers.find()

number_of_customers_acquired_from_events = 0
number_of_customers_acquired_from_ads = 0
number_of_customers_acquired_from_wom = 0
for all_customers in get_all_customers:
    for key, value in all_customers.items():
        if key == "ref" and value == "events":
            number_of_customers_acquired_from_events += 1
        elif key == "ref" and value == "ads":
            number_of_customers_acquired_from_ads += 1
        elif key == "ref" and value == "wom":
            number_of_customers_acquired_from_wom += 1

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

labels = ["Events", "Advertisements", "Word of mouth"]
values = [number_of_customers_acquired_from_events, number_of_customers_acquired_from_ads, number_of_customers_acquired_from_wom]
colors = ["red", "blue", "violet"]

pyplot.pie(values, labels = labels, colors = colors)
pyplot.axis("equal")
pyplot.show()    