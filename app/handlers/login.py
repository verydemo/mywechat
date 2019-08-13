import tornado
import json
import jwt
import datetime
import time

from .base import BaseHandler

class AuthHandler(BaseHandler):

    def get(self):
        self.write('Auth!!')
        self.finish()

    def post(self):

        try:
            username = self.get_argument("username")
            password=self.get_argument("password")
        except:
            self.set_status(403)
            return

        if password:
            t_user=self.objmongo.db["user"]
            result=t_user.find_one({'username':username,'password':password})
            if result is not None and result["_id"] is not None:
                dataToken = {"id": result["_id"], "username": username}
                header={'type':'JWT',"alg":"HS256",'userid':result["_id"]}
                playload={'header':header,'iss':'zjl','exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*12),'iat':datetime.datetime.utcnow()}
                token = jwt.encode(playload, "lxlzjl", algorithm='HS256').decode('ascii')
                status = "A10"
                res = "login success"
            else:
                token = None
                status = "B10"
                res = "wrong username or password."

        self.write({'username':username, "status": status,"msg":res, "token": token})
        self.finish()