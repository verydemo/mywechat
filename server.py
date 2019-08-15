import os,sys
import tornado.ioloop
import tornado.web

import app.handlers.login as ah_login
import app.handlers.register as ah_register
import app.handlers.test as ah_test
import app.handlers.wechatGroup as ah_wechatGroup
import app.handlers.wechatBusiness as ah_wechatBusiness
import app.handlers.wechatPersonal as ah_wechatPersonal
import app.handlers.wechatThePublic as ah_wechatThePublic
import app.handlers.wechatArticle as ah_wechatArticle

import app.objects.objmongodb as ao_objmongodb
import app.utils.util as au_util

config = au_util.getConfig()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/login", ah_login.AuthHandler),
            (r"/register", ah_register.registerHandler),
            (r"/test", ah_test.testHandler),
            (r"/wechatGroup", ah_wechatGroup.wechatGroupHandler),
            (r"/wechatBusiness", ah_wechatBusiness.wechatBusinessHandler),
            (r"/wechatPersonal", ah_wechatPersonal.wechatPersonalHandler),
            (r"/wechatThePublic", ah_wechatThePublic.wechatThePublicHandler),
            (r"/wechatArticle", ah_wechatArticle.wechatArticleHandler),
        ]
        self.config = config
        settings = dict(
            debug=self.config["debug"],
            )
        tornado.web.Application.__init__(self, handlers, **settings)
        mongodb = self.config["mongodb"]
        self.objmongo = ao_objmongodb.objmongo(
            mongodb["db_host"], mongodb["db_port"], mongodb["db_name"])


def main(port):
    application = Application()
    print("port is {}".format(port))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    try:
        port=int(sys.argv[1])
    except:
        port=8888
    main(port)
