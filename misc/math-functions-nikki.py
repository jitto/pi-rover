def fib(n):
     a, b = 0, 1
     while a < n:
             print a,
             a, b = b, a+b

def cube_volume(n):
	return n ** 3

def cube_area(n):
	return n * n * 6

def triangle_area(height, basewidth):
 	return (height * basewidth) /2

def pyramid_area(triangleheight, basewidth):
	d=(triangleheight * basewidth) /2 * 4
	return d + (basewidth ** 2)


def pyramid_volume(pyramidheight, basewidth):
	return (basewidth ** 2) * pyramidheight /3



import math



def cylinder_volume(width, height):
	return (width /2) ** 2 * math.pi * height

import math


def cylinder_area(width, height):
	d= width * math.pi
	c= (width /2) ** 2 * math.pi
	return (d * height) + (c * 2) 
	
