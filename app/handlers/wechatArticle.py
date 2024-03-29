import tornado
import json
import datetime
from dateutil import parser

import app.utils.auth as au_auth
from .base import BaseHandler
import app.utils.mogon as au_mogon


@au_auth.jwtauth
class wechatArticleHandler(BaseHandler):

    def get(self, id=0):
        if id == 0:
            t_wechatArticle = self.objmongo.db["wechatArticle"]
            # qtime = parser.parse((datetime.datetime.now() - datetime.timedelta(seconds=60*60*24*30)).isoformat())
            # query = {"time": {"$gte": qtime}}
            recommend= self.get_argument("recommend", "")
            query,data,lists={},{},[]
            if recommend=="1":
                collection=t_wechatArticle.find().sort('count',-1).limit(15)
                for i in collection:
                    i["time"]=i["time"].strftime("%Y-%m-%d")
                    lists.append(i)
                self.gen_data("200","success",lists)
                self.finish()
            else:
                page= self.get_argument("page", "")
                if self.get_argument("industry", "") != "":
                    query['industry'] = self.get_argument("industry", "")
                if self.get_argument("area", "") != "":
                    query['area'] = self.get_argument("area", "")
                if page != "" and page.isdigit():
                    page=int(page)
                else:
                    page=1
                data["count"]=t_wechatArticle.count()
                collection=t_wechatArticle.find(query).sort('time',-1).limit(36).skip((page-1)*36)
                for i in collection:
                    i["time"]=i["time"].strftime("%Y-%m-%d")
                    lists.append(i)
                data["page"]=page
                data["data"]=lists
                self.gen_data("200","success",data)
                self.finish()
        else:
            try:
                if int(id) > 0:
                    id = int(id)
                    t_wechatArticle = self.objmongo.db["wechatArticle"]
                    query = {'_id': id}
                    t_wechatArticle.find_and_modify({"_id": id}, {"$inc": {"count": 1}}, safe=True, new=True)
                    wechatArticle = t_wechatArticle.find_one(query)
                    wechatArticle['time']=wechatArticle['time'].strftime("%Y-%m-%d") 
                    self.gen_data("200", "success", wechatArticle)
                    self.finish()
                else:
                    self.gen_data("105", "fail", "para error")
                    self.finish()
            except:
                self.gen_data("104", "fail", "para error")
                self.finish()

    def post(self):
        data = {}
        try:
            data["username"] = self.get_argument("username", "")
            if data["username"] == "":
                self.gen_data("101", "fail", "")
                self.finish()
                return
            data["column"] = self.get_argument("column", "")
            data["title"] = self.get_argument("title", "")
            data["Content"] = self.get_argument("Content", "")
            data["CoverImg"] = self.get_file("CoverImg", data["username"])
            data["time"] = parser.parse(datetime.datetime.now().isoformat())
            data['count']=1
            data['type']='wechatArticle'
        except:
            self.gen_data("102", "fail", "")
            self.finish()
            return
        user = data["username"]

        t_wechatArticle = self.objmongo.db["wechatArticle"]
        id = au_mogon.getNextValue(self.objmongo.db, "wechatArticle")
        data["_id"] = id
        result = t_wechatArticle.insert_one(data)
        if result is not None:
            res = {"user": user}
            self.gen_data("200", "success", res)
            self.finish()
        else:
            res = {"user": user}
            self.gen_data("103", "fail", res)
            self.finish()
