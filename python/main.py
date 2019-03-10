#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from speedtester import speedtester
from db_handler import execute
from time import sleep
import json

#---------------------Variablen--------------------#

# Datenbank Name
db_name = "speedtests.db"

#Timer zum Einstell für die Startzeit: start: <Minuten der Stunde>, interval: <Intervall in Minuten>
time_interval = {"start": "00", "interval": "60"}

#--------------------SQL Statements----------------#
sqls_delete_table = "DROP TABLE IF EXISTS results;"

sqls_init_table = """CREATE TABLE IF NOT EXISTS results(
                    id INTEGER PRIMARY KEY,
                    download REAL,
                    upload REAL,
                    ping REAL,
                    lat REAL,
                    lon REAL,
                    city text,
                    country text,
                    sponsor text,
                    datetime text,
                    up REAL,
                    down REAL
                    );
                """

sql_insert_table = """INSERT INTO results(download, upload, ping, lat, lon, city, country, sponsor, datetime, up, down)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?);
                        """

#TODO where clause mit Zeit Intervall für individuelle Abfrage
sql_select_table = "SELECT * FROM results"

#---------------------Main--------------------#



def db_query():
    results = dict()

    rows = execute(db_name, sql_select_table, None)
    for row in rows:
        results[row[0]] = row

    return json.dumps(results)


def start_speedtest():

    execute(db_name, sqls_init_table, None)

    start = time_interval["start"]
    current_start = datetime.now().strftime('%M')
    if start > current_start:
        start_time = datetime.now().strftime('%H') + ":" + start
    else:
        start_time = datetime.now() + timedelta(hours=1)
        start_time = start_time.strftime('%H') + ":" + start

    print("---> warte auf Start um : %s Uhr" % start_time)

    while True:


        current_min = datetime.now().strftime('%M')
        if current_min == start:
            print("---> beginne Speedtest")

            min = datetime.now().strftime("%M")
            next = int(min) + int(time_interval["interval"])
            if next < 60:
                next_time = datetime.now().strftime("%H")
                next_time = next_time + ":" + str(next)
                start = str(next)
            else:
                next = next - 60
                next_time = datetime.now() + timedelta(hours=1)
                next_time = next_time.strftime("%H")
                next_time = next_time + ":" + str(next)
                start = str(next)


            test = speedtester()
            results = test[0]
            duration = test[1]
            values = (results["download"], results["upload"], results["ping"], results["lat"], results["lon"], results["name"], results["country"],
                     results["sponsor"], results["datetime"], results["up"], results["down"])

            print("---> Schreibe in Datenbank %s : %s" % (db_name, values))
            execute(db_name, sql_insert_table, values)


            print("---> nächster Speedtest um : %s Uhr" % next_time)
            sleep(int(time_interval["interval"]) * 60 - duration)





