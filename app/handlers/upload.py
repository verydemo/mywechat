import tornado
import json

import app.utils.auth as au_auth
from .base import BaseHandler

# @au_auth.jwtauth
class uploadHandler(BaseHandler):

    def post(self):
        try:
            username=self.get_argument("username","")
            if username!="":
                sharePath=self.get_filenew("upfile",username)
                print(sharePath)
            else:
                self.gen_data('101','fail','')
                return 
        except:
            self.gen_data('102','fail','')
            return

        if sharePath:
            self.gen_data('200','success',sharePath)
        else:
            self.gen_data('103','fail','')

