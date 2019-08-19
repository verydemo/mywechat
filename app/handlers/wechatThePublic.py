import tornado
import json,traceback
import datetime
from dateutil import parser

import app.utils.auth as au_auth
from .base import BaseHandler
import app.utils.mogon as au_mogon

@au_auth.jwtauth
class wechatThePublicHandler(BaseHandler):

    def get(self,id=0):
        if id==0:
            t_wechatThePublic=self.objmongo.db["wechatThePublic"]
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
            data["count"]=t_wechatThePublic.count()
            collection=t_wechatThePublic.find(query).sort('time',1).limit(36).skip((page-1)*36)
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
                    t_wechatThePublic=self.objmongo.db["wechatThePublic"]
                    t_wechatThePublic.find_and_modify({"_id": id}, {"$inc": {"count": 1}}, safe=True, new=True)                    
                    wechatThePublic=t_wechatThePublic.find_one({"_id":id})
                    wechatThePublic['time']=wechatThePublic['time'].strftime("%Y-%m-%d") 
                    self.gen_data("200","success",wechatThePublic)
                    self.finish()
                else:
                    self.gen_data("105","fail","para error")
                    self.finish()
            except:
                traceback.print_exc()
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
            data["publicName"] = self.get_argument("publicName","")
            data["publicId"] = self.get_argument("publicId","")
            data["publicCoverImg"]=self.get_file("publicCoverImg",data["username"])
            data["publicQRImg"]=self.get_file("publicQRImg",data["username"])
            data["introducer"] = self.get_argument("introducer","")
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
        t_wechatThePublic=self.objmongo.db["wechatThePublic"]
        id=au_mogon.getNextValue(self.objmongo.db,"wechatThePublic")
        data["_id"]=id      
        result=t_wechatThePublic.insert_one(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()