import pymongo
import json

def getConfig():
    with open('config.json','r',encoding='utf-8') as f:
        return json.loads(f.read())

def main():
    config=getConfig()
    db_host=config["mongodb"]["db_host"]
    db_port=config["mongodb"]["db_port"]
    db_name=config["mongodb"]["db_name"]
    client=pymongo.MongoClient(host=db_host,port=db_port)
    db=client[db_name]

    # clear db data
    db.command("dropDatabase")

    # set collection user initial value
    db.id.insert_one({'id_name':'user','sequence_value':0})
    db.id.insert_one({'id_name':'wechatArticle','sequence_value':0})
    db.id.insert_one({'id_name':'wechatBusiness','sequence_value':0})
    db.id.insert_one({'id_name':'wechatGroup','sequence_value':0})
    db.id.insert_one({'id_name':'wechatPersonal','sequence_value':0})
    db.id.insert_one({'id_name':'wechatThePublic','sequence_value':0})
    db.id.insert_one({'id_name':'file','sequence_value':0})
    db.id.insert_one({'id_name':'upfile','sequence_value':0})

    # set index
    db["wechatArticle"].create_index([("industry", 1), ("area", 1)])
    db["wechatBusiness"].create_index([("industry", 1), ("area", 1)])
    db["wechatGroup"].create_index([("industry", 1), ("area", 1)])
    db["wechatPersonal"].create_index([("industry", 1), ("area", 1)])
    db["wechatThePublic"].create_index([("industry", 1), ("area", 1)])

if __name__ == "__main__":
    main()