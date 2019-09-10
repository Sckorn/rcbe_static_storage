#!/usr/bin/env python

import tornado.web
import os

class X3dHandler(tornado.web.RequestHandler):

    def initialize(self, files_path):
        self._files_path = files_path

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Content-Type", "text/xml")

    def get(self, file_nane):
        path = self._files_path + "/" + file_nane + ".x3d"

        if os.path.isfile(path):
            with open(path, 'r') as content_file:
                content = content_file.read()
                self.write(content)
                self.finish()
        else:
            self.write("")
            self.send_error(404)