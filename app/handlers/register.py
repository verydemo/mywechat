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
            self.set_status(403)
            return

        if password:
            t_user=self.objmongo.db["user"]
            logined=t_user.find({'username':login})
            if logined.count() == 0 :
                id=au_mogon.getNextValue(self.objmongo.db,"user")
                result=t_user.insert({'_id':id ,'username':login,'password':password})
                if result is not None :
                    dataToken = {"id": id, "login": data["username"]}
                    status = 200
                    res = dataToken
                else:
                    status = 102
                    res = "Invalid Username or Password."
            else:
                status = 101
                res = "Username has already been registered"

        self.write({"data": res, "status": status})
        self.finish()