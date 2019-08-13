import os
import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web

import app.handlers.login as ah_login
import app.handlers.register as ah_register
import app.handlers.test as ah_test
import app.objects.objmongodb as ao_objmongodb

define("debug", default=True, help="Executar o servidor em modo debug", type=bool)
define("port", default=8080, help="api post", type=int)
define("db_port", default=27017, help="db post", type=int)
define("db_host", default="192.168.112.129", help="mongodb IP")
define("db_name", default="wechat", help="mongodb db name")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/login", ah_login.AuthHandler),
            (r"/register", ah_register.registerHandler),
            (r"/test", ah_test.testHandler),
        ]
        settings = dict(
            debug=options.debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # create mongodb object and Init data
        self.objmongo = ao_objmongodb.objmongo(
            options.db_host, options.db_port, options.db_name)


def main():
    tornado.options.parse_command_line()
    application = Application()
    print("port is {}".format(options.port))
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
