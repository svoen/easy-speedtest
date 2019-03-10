#!/usr/bin/env python
# -*- coding: utf-8 -*-


from http.server import HTTPServer,  BaseHTTPRequestHandler
from db_handler import execute

from threading import Thread
import json

import main




class Serv(BaseHTTPRequestHandler):
    print("---> starte Http-Server")
    def do_GET(self):
        try:

            response = main.db_query()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')


        except:
            response = "Nichts gefunden..."
            self.send_response(404)


        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))






httpd = HTTPServer(('localhost', 8080), Serv)


