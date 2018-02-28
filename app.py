#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask

import RPi.GPIO as GPIO
import time

app = Flask(__name__)

relay_ch1 = 19
relay_ch2 = 26
relay_ch3 = 20
relay_ch4 = 21
repeat = 0

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


@app.route('/')
def index():
  return app.send_static_file('templates/index.html')


@app.route('/on')
def on():
  GPIO.output(relay_ch1, GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(relay_ch1, GPIO.HIGH)
  return ''


@app.route('/repeat')
def repeat():
  repeat_task(relay_ch1, 5)
  return ''


@app.route('/off')
def off():
  global repeat
  repeat = 0
  GPIO.output(relay_ch1, GPIO.LOW)
  time.sleep(6)
  GPIO.output(relay_ch1, GPIO.HIGH)
  return ''


def repeat_task(channel, repeat_count):
  print("Repeating ", repeat_count, " times")
  global repeat
  repeat = repeat_count
  while repeat > 0:
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.5)
    print("Repeat on")
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(5)
    repeat = repeat - 1


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
