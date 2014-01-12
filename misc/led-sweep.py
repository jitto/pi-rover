#!/usr/bin/python

import piface.pfio as pfio
pfio.init()

import time

while True:

  led_number=0

  while (led_number < 8):
    pfio.LED(led_number).turn_on()
    time.sleep(0.5)
    pfio.LED(led_number).turn_off() 
    led_number=led_number+1
    
    if led_number == 7:
      while (led_number > 0):
        pfio.LED(led_number).turn_on()
        time.sleep(0.5)
        pfio.LED(led_number).turn_off()
        led_number=led_number-1
    
        if led_number == 8:
          led_number=0


