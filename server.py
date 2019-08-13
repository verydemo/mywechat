import os
import tornado.ioloop
import tornado.web

import app.handlers.login as ah_login
import app.handlers.register as ah_register
import app.handlers.test as ah_test
import app.objects.objmongodb as ao_objmongodb
import app.utils.util as au_util

config = au_util.getConfig()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/login", ah_login.AuthHandler),
            (r"/register", ah_register.registerHandler),
            (r"/test", ah_test.testHandler),
        ]
        self.config = config
        settings = dict(
            debug=self.config["debug"],
            )
        tornado.web.Application.__init__(self, handlers, **settings)
        mongodb = self.config["mongodb"]
        self.objmongo = ao_objmongodb.objmongo(
            mongodb["db_host"], mongodb["db_port"], mongodb["db_name"])


def main():
    application = Application()
    print("port is {}".format(config["port"]))
    application.listen(config["port"])
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
