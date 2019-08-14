import tornado
import json
import jwt
from .base import BaseHandler
import app.utils.mogon as au_mogon

class registerHandler(BaseHandler):

    def post(self):
        data={}
        data["username"] = self.get_argument("username")
        data["password"]=self.get_argument("password")
        try:
            login = data["username"]
            password = data["password"]
        except:
            res = "Invalid Username or Password."
            self.gen_data("101","fail",res)
            self.finish()
            return

        if password:
            t_user=self.objmongo.db["user"]
            logined=t_user.find({'username':login})
            if logined.count() == 0 :
                id=au_mogon.getNextValue(self.objmongo.db,"user")
                result=t_user.insert({'_id':id ,'username':login,'password':password})
                if result is not None :
                    res = 'register success'
                    self.gen_data("200","success",res)
                else:
                    res = "Invalid Username or Password."
                    self.gen_data("102","fail",res)
            else:
                res = "Username has already been registered"
                self.gen_data("103","fail",res)
        self.finish()