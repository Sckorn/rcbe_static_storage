# Author: Andrey Troitskiy

import tornado.web
import os

class WebConfigHandler(tornado.web.RequestHandler):

    def initialize(self, port):
        self.port = port

    def get(self):
        addr = self.request.host.split(':')[0];
        self.write("var rosbridge_port={};\n".format(self.port))
        self.write("var rosbridge_addr='{}';\n".format(addr))
        self.write("var rosbridge_url='ws://{}:{}';\n".format(addr, self.port))
        self.write("var OPER_HOME='{}';\n".format(os.environ.get('OPER_HOME','/root')))
        self.write("var CATKIN_WS='{}';\n".format(os.environ.get('CATKIN_WS','/root/ws_moveit')))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
