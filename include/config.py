#!/usr/bin/python
import psycopg2
import os
import json
from include.filedir import dirFile


config = dirFile()

def connect():
    connection = None
    try:
        connection = psycopg2.connect(user = config.get('user'),
                                        password = config.get('password'),
                                        host = config.get('host'),
                                        port = config.get('port'),
                                        database = config.get('database'))
        return connection
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        return connection