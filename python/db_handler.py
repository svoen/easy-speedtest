#!/usr/bin/env python
# -*- coding: utf-8 -*-

##TEST##
import sqlite3


def execute(db_name, sql, values):
    """ create a database connection to a SQLite database """
    try:


        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        if values is None:
            c.execute(sql)
            rows = c.fetchall()
            return rows

        else:
            c.execute(sql, values)
            conn.commit()

        conn.close()


    except Error as e:
        print(e)


























