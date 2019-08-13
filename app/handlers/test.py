import tornado
import json

import app.utils.auth as au_auth

@au_auth.jwtauth
class testHandler(tornado.web.RequestHandler):

    def get(self):
        
        if self.request.headers.get('Authorization'):
            self.write({"status":200,"msg":'ok'})