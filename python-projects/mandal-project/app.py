#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDHT_v1.py
#
#  Created by MJRoBot.org
#  10Jan18

'''
    RPi WEb Server for captured data with Graph plot
'''

import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

DB_FILENAME = 'mandal_sensor.db'


def get_voltage_current_data(numSamples=10000):
    with sqlite3.connect(DB_FILENAME) as conn:
        curs = conn.cursor()
        curs.execute(
            "SELECT * FROM voltage_current ORDER BY timestamp DESC LIMIT "
            + str(numSamples))
        data = curs.fetchall()
        primary_key, voltage, current, timestamp = [], [], [], []
        for row in reversed(data):
            primary_key.append(row[0])
            voltage.append(row[1])
            current.append(row[2])
            timestamp.append(row[3])
        curs.close()
        return primary_key, voltage, current, timestamp


@app.route("/")
def index():
    primary_key, voltage, current, timestamp = get_voltage_current_data()
    voltage_data = [[t, volt] for t, volt in zip(timestamp, voltage)]
    current_data = [[t, amp] for t, amp in zip(timestamp, current)]
    return render_template('index.html',
                           voltage_data=voltage_data,
                           current_data=current_data)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80, debug=False)
    app.run(debug=True)
