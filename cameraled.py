#!/usr/bin/env python

__author__ = "Yohann Chemtob"
__license__ = "WTFPL"
__version__ = "0.1"

from picamera import PiCamera
import time
import RPi.GPIO as GPIO

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


print('Press Ctrl-C to quit.')
starttime=time.time()

while True:
    GPIO.output(17, GPIO.HIGH)
    tmpnamefile = time.strftime("%d%m%Y_%H.%M.%S.jpg", time.gmtime())
    camera.capture('/home/pi/timelapse01/'+tmpnamefile)
    GPIO.output(17, GPIO.LOW)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

