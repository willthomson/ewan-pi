#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

import flask
import RPi.GPIO as GPIO
import time
import atexit

app = Flask(__name__)

relay_ch1 = 19
relay_ch2 = 26
relay_ch3 = 20
relay_ch4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Init all of the relay channels.
GPIO.setup(relay_ch1, GPIO.OUT)
GPIO.setup(relay_ch2, GPIO.OUT)
GPIO.setup(relay_ch3, GPIO.OUT)
GPIO.setup(relay_ch4, GPIO.OUT)

# Make sure all the relays are off at startup.
GPIO.output(relay_ch1, GPIO.HIGH)
GPIO.output(relay_ch2, GPIO.HIGH)
GPIO.output(relay_ch3, GPIO.HIGH)
GPIO.output(relay_ch4, GPIO.HIGH)

def handle_cron():
  print('repeat', flask.g.repeat)
  if(flask.g.repeat > 0):
    on()
    flask.g.repeat = flask.g.repeat - 1
    if(flask.g.repeat == 0):
      scheduler.pause()
  elif(flask.g.repeatrepeat == -1):
    on()
  else:
    flask.g.repeat = 0
    scheduler.pause()

scheduler = BackgroundScheduler()
scheduler.start(paused=True)
scheduler.add_job(
    func=handle_cron,
    trigger=IntervalTrigger(seconds=5), #minutes=19),
    id='cron_job',
    name='Ewan timer',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

@app.route('/')
def index():
  return app.send_static_file('templates/index.html')


@app.route('/on')
def on():
  GPIO.output(relay_ch1, GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(relay_ch1, GPIO.HIGH)
  return ''


@app.route('/repeat/<repeat_count>')
def repeat(repeat_count):
  print('repeat_count', repeat_count)  
  flask.g.repeat = repeat_count
  scheduler.resume()
  return ''


@app.route('/off')
def off():
  flask.g.repeat = 0
  scheduler.pause()
  GPIO.output(relay_ch1, GPIO.LOW)
  time.sleep(6)
  GPIO.output(relay_ch1, GPIO.HIGH)
  return ''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')















































