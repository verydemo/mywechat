# -*- coding: utf-8 -*-

import tornado
import json
import jwt
from .base import BaseHandler

class registerHandler(BaseHandler):

    def post(self):
        data={}
        data["username"] = self.get_arguments("username")
        data["password"]=self.get_arguments("password")
        try:
            login = data["username"]
            password = data["password"]
        except:
            self.set_status(403)
            return

        if password:
            t_user=self.objmongo.db["user"]
            result=t_user.insert({'_id':self.objmongo.getNextValue("user") ,'username':login,'password':password})
            

        if result is not None :
            dataToken = {"id": result, "login": data["username"]}
            token = jwt.encode(dataToken, "nyxjs", algorithm='HS256').decode('ascii')
            status = True
            res = dataToken
        else:
            token = None
            status = False
            res = "Invalid Username or Password."

        self.write({"data": res, "result": status, "token": token})
        self.finish()