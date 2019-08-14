import tornado
import json

import app.utils.auth as au_auth
from .base import BaseHandler

@au_auth.jwtauth
class wechatThePublicHandler(BaseHandler):

    def get(self):
        
        if self.request.headers.get('Authorization'):
            self.write({"status":200,"msg":'ok'})
    
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
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
        print(data)
        user=data["username"]
        t_wechatThePublic=self.objmongo.db["wechatThePublic"]
        result=t_wechatThePublic.insert(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()