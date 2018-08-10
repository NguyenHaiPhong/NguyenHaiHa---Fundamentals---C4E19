import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds123259.mlab.com:23259/c4e19-cms-app
host = "ds123259.mlab.com"
port = 23259
    
db_name = "c4e19-cms-app"
user_name = "admin"
password = "admin1"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())