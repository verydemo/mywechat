#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import tornado.auth
import tornado.ioloop
from tornado.options import define, options, parse_command_line, parse_config_file
import tornado.web

import app.handlers.main
import app.handlers.project
import app.handlers.auth
import app.handlers.register

# from .objects import objmongodb
import app.objects.objmongodb 

define("debug", default=True, help="Executar o servidor em modo debug", type=bool)
define("port", default=8080, help="api post", type=int)
define("db_port", default=27017, help="db post", type=int)
define("db_host", default="192.168.112.128", help="mongodb IP")
define("db_name", default="wechat", help="mongodb db name")



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", app.handlers.main.MainHandler),
            (r"/auth", app.handlers.auth.AuthHandler),
            (r"/project", app.handlers.project.ProjectHandler),
            (r"/register", app.handlers.register.registerHandler),
        ]
        settings = dict(
            debug = options.debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Connect from db,client
        self.objmongo=app.objects.objmongodb.objmongo(options.db_host,options.db_port,options.db_name)
        self.objmongo.id_increase("user")

def main():
    tornado.options.parse_command_line()
    application = Application()
    print ("port is {}".format(options.port))
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()