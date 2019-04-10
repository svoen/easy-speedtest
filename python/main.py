#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from speedtester import test
from db_handler import execute
from time import sleep
import json

#---------------------Variablen--------------------#

# Datenbank Name
__db_name = "speedtests.db"

# Timer zum Einstell für die Startzeit: start: <Minuten der Stunde>, interval: <Intervall in Minuten>
start = str(input("Start Minute der Stunde [MM]: "))
interval = str(input("Interval in Minuten [MM]: "))
if start == "60":
    start = "00"
if interval == "00":
    interval = "60"
time_interval = {"start": start, "interval": interval}

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
    rows = execute(__db_name, sql_select_table, None)
    for row in rows:
        results[row[0]] = row

    return json.dumps(results)

def wait():
    min_now = datetime.now().strftime('%M')
    if int(time_interval["start"]) > int(min_now):
        start_time = datetime.now().strftime('%H') + ":" + time_interval["start"]
        print("---> warte auf Start um: %s Uhr" % start_time)
        while datetime.now().strftime('%M') != time_interval["start"]:
            pass

    elif min_now == time_interval["start"]:
        print("--->")
    else:
        start_time = datetime.now() + timedelta(hours=1)
        start_time = start_time.strftime('%H') + ":" + time_interval["start"]
        print("---> warte auf Start um: %s Uhr" % start_time)
        while datetime.now().strftime('%M') != time_interval["start"]:
            pass

    return time_interval["start"]

def timer():
    min_now = datetime.now().strftime('%M')
    skip_hour = 0
    next = int(min_now) + int(time_interval["interval"])
    next_hour = (datetime.now() + timedelta(hours=1)).strftime("%H")
    if time_interval["interval"] == "00":
        start = time_interval["interval"]
        next_time = next_hour + ":" + start

        return start, next_time
    else:
        while next >= 60:
            next = next - 60
            skip_hour += 1

        if next < 10:
            start = "0" + str(next)
        else:
            start = str(next)
        next_time = (datetime.now() + timedelta(hours=skip_hour)).strftime("%H") + ":" + start

        return start, next_time


def get_test():
    execute(__db_name, sqls_init_table, None)
    tests = test()
    results = tests[0]
    duration = tests[1]
    values = (results["download"], results["upload"], results["ping"], results["lat"], results["lon"], results["name"], results["country"],
             results["sponsor"], results["datetime"], results["up"], results["down"])

    print("---> Schreibe in Datenbank %s : %s" % (__db_name, values))
    execute(__db_name, sql_insert_table, values)


def start_speedtest():
    start = wait()
    while True:
        if datetime.now().strftime('%M') == start:
            times = timer()
            start = times[0]
            print("")
            next_time = times[1]
            get_test()
            print("---> nächster Speedtest um : %s Uhr" % next_time)
            print("")
            sleep(int(time_interval["interval"]) * 60 - 60)




