import tornado
import json
import datetime
from dateutil import parser


import app.utils.auth as au_auth
from .base import BaseHandler

@au_auth.jwtauth
class wechatPersonalHandler(BaseHandler):

    def get(self):
        t_wechatPersonal=self.objmongo.db["wechatPersonal"]
        qtime=parser.parse((datetime.datetime.utcnow() - datetime.timedelta(seconds=60*60*30)).isoformat())
        wechatPersonals=t_wechatPersonal.find({"time":{"$gte":qtime}},{"_id":0,"time":0})
        wechatPersonals=[i for i in wechatPersonals]
        self.gen_data("200","success",wechatPersonals)
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
            data["time"]=parser.parse(datetime.datetime.utcnow().isoformat())
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
        user=data["username"]
        t_wechatPersonal=self.objmongo.db["wechatPersonal"]
        result=t_wechatPersonal.insert(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()       