import tornado
import json
import traceback

import app.utils.auth as au_auth
from .base import BaseHandler


@au_auth.jwtauth
class wechatArticleHandler(BaseHandler):

    def get(self):

        if self.request.headers.get('Authorization'):
            self.write({"status": 200, "msg": 'ok'})

    def post(self):
        data = {}
        try:            
            data["username"] = self.get_argument("username","")
            if data["username"]=="":
                self.gen_data("101","fail","")
                self.finish()
                return
            data["column"] = self.get_argument("column","")
            data["articleName"] = self.get_argument("articleName","")
            data["articleContent"] = self.get_argument("articleContent","")
            data["articleCoverImg"]=self.get_file("articleCoverImg",data["username"])
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
        print(data)
        user=data["username"]
        t_wechatArticle=self.objmongo.db["wechatArticle"]
        result=t_wechatArticle.insert(data)
        if result is not None :
            res={"user":user}
            self.gen_data("200","success",res)
            self.finish()
        else:
            res={"user":user}
            self.gen_data("103","fail",res)
            self.finish()

