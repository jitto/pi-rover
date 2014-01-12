#!/usr/bin/python


def reverse(word):
	reverse_string = ''
	for position in range (len(word),0,-1) :
		reverse_string = reverse_string + word[position - 1] 
	print reverse_string

reverse('awesome')

