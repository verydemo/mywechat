import pymongo


class objmongo(object):
    def __init__(self,host,port,db):
        self.client = pymongo.MongoClient(host=host,port=port)
        self.db=self.client[db]
        self.ids=self.db["id"]

    def id_increase(self,name):
        self.ids.delete_many({'_id':name})
        self.ids.insert({'_id':name,'sequence_value':0})

    def db(self):
        return self.db
    
    def client(self):
        return self.client

    def getNextValue(self,t_id):
        ret = self.ids.find_and_modify({"_id": t_id}, {"$inc": {"sequence_value": 1}}, safe=True, new=True)
        new = ret["sequence_value"]
        return new
       