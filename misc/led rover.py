Python 2.7.3 (default, Jan 13 2013, 11:20:46) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIO
>>> GPIO.setmode(GPIO.BOARD)
>>> GPIO.setup(16, GPIO.OUT)
>>> GPIO.output(16,True)
>>> 

>>> GPIO.setup(18, GPIO.OUT)
>>> GPIO.output(18, False)
>>> 
