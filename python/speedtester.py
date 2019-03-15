#!/usr/bin/env python
# -*- coding: utf-8 -*-


from speedtest import Speedtest
import ssl
import socket
import time
from datetime import datetime

def test():
    try:
        start_time = time.time()
        ssl._create_default_https_context = ssl._create_unverified_context
        ip = socket.gethostbyname(socket.gethostname())
        #ip = "192.168.178.23"
        host = socket.gethostname()

        print("---> Host: %s %s" % (host, ip))
        print("---> starte Speedtest um: %s Uhr" % datetime.now().strftime("%H:%M"))
        print("---> Speedtest läuft...")
        s = Speedtest(source_address=ip)
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()
        response = s.results.dict()

        download = round(float(response["download"]) / 1048576, 2)
        upload = round(float(response["upload"]) / 1048576, 2)
        ping = round(response["ping"])
        lat = float(response["server"]["lat"])
        lon = float(response["server"]["lon"])
        name = str(response["server"]["name"])
        country = str(response["server"]["country"])
        sponsor = str(response["server"]["sponsor"])
        timestamp = str(response["timestamp"])
        up = round(float(response["bytes_sent"]) / 131072, 2)
        down = round(float(response["bytes_received"]) / 131072, 2)

        result = {"download": download,
                  "upload": upload,
                  "ping": ping,
                  "lat": lat,
                  "lon": lon,
                  "name": name,
                  "country": country,
                  "sponsor": sponsor,
                  "datetime": timestamp,
                  "up": up,
                  "down": down
                  }

        duration = time.time() - start_time
        print("---> Speedtest fertig in %s Sekunden" % round(duration))

        return result, duration

    except Exception as error:
        raise error