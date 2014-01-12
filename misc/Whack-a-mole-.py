#!/usr/bin/python

import piface.pfio as pfio
import time
import random

pfio.init()

g='level '

f=1


	

for i in range(0,6):
	print g
	print f
	sleep_time = 5
	def player_pressed_button_in_time(button_number, time_to_wait) :
		for x in range (0, time_to_wait * 10):
			if c:
				return True
				time.sleep (0.1)
				return False

				while sleep_time > 0:
					led_number = random.randint(4, 7)
					button_number = 7 - led_number
					pfio.LED(led_number).turn_on()
					if player_pressed_button_in_time(button_number, sleep_time) :
						sleep_time = sleep_time - 1  
					else :
						sleep_time = sleep_time + 1 
						pfio.LED(led_number).turn_off()
					if sleep_time == 1:
						f=f+1



#make button mumber align with led_number
	#make sure the same LED is not turned on twice in a row 
	#make sure the player cant cheat by keeping a button pressed

