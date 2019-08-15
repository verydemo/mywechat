import tornado
import time
import os

class BaseHandler(tornado.web.RequestHandler):

    @property
    def objmongo(self):
        return self.application.objmongo

    def options(self):
        pass

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'OPTIONS, POST, GET, PATCH, DELETE, PUT')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')

    # get file return sharepath
    def get_file(self,name,key):
        files = self.request.files
        avatars = files.get(name)
        toPath,sharePath="",""
        toFloder=self.application.config["toFloder"]
        shareFloder=self.application.config["shareFloder"]
        for avatar in avatars:
            filename = avatar.get('filename')
            data = avatar.get('body')
            t=time.time()
            toPath=os.path.join(str(toFloder),str(t)+str(key)+os.path.splitext(filename)[1])
            with open(toPath,'wb') as writer:
                writer.write(data)
            sharePath=os.path.join(str(shareFloder),str(t)+str(key)+os.path.splitext(filename)[1])
        if sharePath!="":
            return sharePath 
        else:
            return False
    
    def gen_data(self,statu,msg,res):
        self.write({"statu":statu,"msg":msg,"data":res})