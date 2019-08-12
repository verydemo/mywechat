import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Olá Mundo!!')