def fib(n):
	count=0     
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b
		count= count + 1
	print '\n'
	print count
