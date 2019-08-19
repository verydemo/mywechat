import tornado
import json
import datetime
from dateutil import parser


import app.utils.auth as au_auth
from .base import BaseHandler
import app.utils.mogon as au_mogon

@au_auth.jwtauth
class wechatPersonalHandler(BaseHandler):
            
    def get(self,id=0):
        if id==0:
            t_wechatPersonal=self.objmongo.db["wechatPersonal"]
            # qtime=parser.parse((datetime.datetime.now() - datetime.timedelta(seconds=60*60*24*30)).isoformat())
            # query = {"time": {"$gte": qtime}}
            page= self.get_argument("page", "")
            query,data,lists={},{},[]
            if self.get_argument("industry", "") != "":
                query['industry'] = self.get_argument("industry", "")
            if self.get_argument("area", "") != "":
                query['area'] = self.get_argument("area", "")
            if page != "" and page.isdigit():
                page=int(page)
            else:
                page=1
            data["count"]=t_wechatPersonal.count()
            collection=t_wechatPersonal.find(query).sort('time',1).limit(36).skip((page-1)*36)
            for i in collection:
                i["time"]=i["time"].strftime("%Y-%m-%d")
                lists.append(i)
            data["page"]=page
            data["data"]=lists
            self.gen_data("200","success",data)
            self.finish()
        else:
            try:
                if int(id)>0:
                    id=int(id)
                    t_wechatPersonal=self.objmongo.db["wechatPersonal"]
                    t_wechatPersonal.find_and_modify({"_id": id}, {"$inc": {"count": 1}}, safe=True, new=True)
                    wechatPersonal=t_wechatPersonal.find_one({"_id":id})
                    wechatPersonal['time']=wechatPersonal['time'].strftime("%Y-%m-%d") 
                    self.gen_data("200","success",wechatPersonal)
                    self.finish()
                else:
                    self.gen_data("105","fail","para error")
                    self.finish()
            except:
                self.gen_data("104","fail","para error")
                self.finish()


    def post(self):
        data = {}
        try:
            data["username"] = self.get_argument("username","")
            if data["username"]=="":
                self.gen_data("101","fail","")
                self.finish()
                return
            data["industry"] = self.get_argument("industry","")
            data["area"] = self.get_argument("area","")
            data["wechat"] = self.get_argument("wechat","")
            data["wechatIntroduction"] = self.get_argument("wechatIntroduction","")
            data["wechatHeadImg"]=self.get_file("wechatHeadImg",data["username"])
            data["wechatQRImg"]=self.get_file("wechatQRImg",data["username"])
            data["name"] = self.get_argument("name","")
            data["phone"] = self.get_argument("phone","")
            data["qq"] = self.get_argument("qq","")
            data["time"]=parser.parse(datetime.datetime.now().isoformat())
            data['count']=1
            data['type']='wechatPersonal'
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
        user=data["username"]
        t_wechatPersonal=self.objmongo.db["wechatPersonal"]
        id=au_mogon.getNextValue(self.objmongo.db,"wechatPersonal")
        data["_id"]=id      
        result=t_wechatPersonal.insert_one(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()       