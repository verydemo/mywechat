import tornado
import json
import datetime
from dateutil import parser

import app.utils.auth as au_auth
from .base import BaseHandler


@au_auth.jwtauth
class wechatArticleHandler(BaseHandler):

    def get(self):
        t_wechatArticle=self.objmongo.db["wechatArticle"]
        qtime=parser.parse((datetime.datetime.utcnow() - datetime.timedelta(seconds=60*60*30)).isoformat())
        wechatArticles=t_wechatArticle.find({"time":{"$gte":qtime}},{"_id":0,"time":0})
        wechatArticles=[i for i in wechatArticles]
        self.gen_data("200","success",wechatArticles)
        self.finish()

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
            data["time"]=parser.parse(datetime.datetime.utcnow().isoformat())
        except:
            self.gen_data("102","fail","")
            self.finish()
            return
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

