#!/usr/local/bin/python3
# Filename: new-date.py
import datetime

def get_yesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday