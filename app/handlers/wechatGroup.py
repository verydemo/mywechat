import tornado
import json
import datetime
from dateutil import parser


import app.utils.auth as au_auth
from .base import BaseHandler


@au_auth.jwtauth
class wechatGroupHandler(BaseHandler):

    def get(self):
        t_wechatGroup=self.objmongo.db["wechatGroup"]
        qtime=parser.parse((datetime.datetime.utcnow() - datetime.timedelta(seconds=60*60*30)).isoformat())
        wechatGroups=t_wechatGroup.find({"time":{"$gte":qtime}},{"_id":0,"time":0})
        wechatGroups=[i for i in wechatGroups]
        self.gen_data("200","success",wechatGroups)
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
            data["time"]=parser.parse(datetime.datetime.utcnow().isoformat())
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
        user=data["username"]
        t_wechatGroup=self.objmongo.db["wechatGroup"]
        result=t_wechatGroup.insert(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()

