#!/usr/bin/python

import piface.pfio as pfio
import time

pfio.init()

for i in range(1,5):
  pfio.write_output(0b00100010)
  time.sleep(.1)
  pfio.write_output(0b01000100)
  time.sleep(.1)
  pfio.write_output(0b00010001)
  time.sleep(.1)
  pfio.write_output(0b10001000)
  time.sleep(.1)


pfio.write_output(0b00000000)
