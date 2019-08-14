import pymongo

# Gen increment id
def getNextValue(db,id_name):
    ret = db.id.find_and_modify({"id_name": id_name}, {"$inc": {"sequence_value": 1}}, safe=True, new=True)
    new = ret["sequence_value"]
    return new

# Clear single or multiple collection data
def clearColldata(db,collection_names):
    for name in collection_names:
        ret=db[name].delete_many({}) 

# 
def initData(db):
    db.command("dropDatabase")
    clearColldata(db,["user","id"])
    db.id.insert({'id_name':'user','sequence_value':0})


