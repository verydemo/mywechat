import pymongo

client=pymongo.MongoClient(host='192.168.112.129',port=27017)

db=client.wechat

# clear db data
db.command("dropDatabase")

# set collection user initial value
db.id.insert({'id_name':'user','sequence_value':0})

# set index
# collection.ensure_index('user_name', unique=True)
# collection.create_index([("word", DESCENDING), ("objURL", ASCENDING)], unique=True)

# db[""].ensure_index('username', unique=True)
# db[""].ensure_index('', unique=True)