import pymongo
import app.utils.mogon as au_mogon

class objmongo(object):
    def __init__(self,host,port,db):
        self.client = pymongo.MongoClient(host=host,port=port)
        self.db=self.client[db]
        self.id=self.db["id"]
        au_mogon.initData(self.db)

