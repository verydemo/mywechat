import tornado
import json,traceback
import datetime
from dateutil import parser


import app.utils.auth as au_auth
from .base import BaseHandler
import app.utils.mogon as au_mogon


@au_auth.jwtauth
class wechatGroupHandler(BaseHandler):

    def get(self,id=0):
        if id==0:
            t_wechatGroup=self.objmongo.db["wechatGroup"]
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
            data["count"]=t_wechatGroup.count()
            collection=t_wechatGroup.find(query).sort('time',1).limit(36).skip((page-1)*36)
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
                    t_wechatGroup=self.objmongo.db["wechatGroup"]
                    t_wechatGroup.find_and_modify({"_id": id}, {"$inc": {"count": 1}}, safe=True, new=True)
                    wechatGroup=t_wechatGroup.find_one({'_id':id})
                    wechatGroup['time']=wechatGroup['time'].strftime("%Y-%m-%d") 
                    self.gen_data("200","success",wechatGroup)
                    self.finish()
                else:
                    self.gen_data("105","fail","para error")
                    self.finish()
            except:
                trac
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
            data["groupName"] = self.get_argument("groupName","")
            data["groupIntroduction"] = self.get_argument("groupIntroduction","")
            data["groupHeadImg"]=self.get_file("groupHeadImg",data["username"])
            data["groupQRImg"]=self.get_file("groupQRImg",data["username"])
            data["groupMasterwechat"] = self.get_argument("groupMasterwechat","")
            data["groupMasterQRImg"] = self.get_file("groupMasterQRImg",data["username"])
            data["name"] = self.get_argument("name","")
            data["phone"] = self.get_argument("phone","")
            data["qq"] = self.get_argument("qq","")
            data["time"]=parser.parse(datetime.datetime.now().isoformat())
            data['count']=1
            data['type']='wechatGroup'
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
        user=data["username"]
        t_wechatGroup=self.objmongo.db["wechatGroup"]
        id=au_mogon.getNextValue(self.objmongo.db,"wechatGroup")
        data["_id"]=id
        result=t_wechatGroup.insert_one(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()

