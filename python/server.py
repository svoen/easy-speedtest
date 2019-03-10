#!/usr/bin/env python
# -*- coding: utf-8 -*-


from http.server import HTTPServer,  BaseHTTPRequestHandler
from db_handler import execute

from threading import Thread
import json

import main




class Serv(BaseHTTPRequestHandler):
    print("---> start Server")
    def do_GET(self):
        try:

            file_to_open = main.db_query()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')


        except:
            file_to_open = "Nichts gefunden..."
            self.send_response(404)


        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))






httpd = HTTPServer(('localhost', 8080), Serv)


