# -*-coding:utf-8 -*-

import math

def get_proper_divisors(number):
	""" 
	Returns a list of all positive proper divisors of integer num.
	"""
	if number == 1:
		return []
	else:
		proper_divisors = set([1])
		for i in xrange(2, int(math.sqrt(number))+1):
			if number%i == 0:
				proper_divisors.update((i, number/i))
		return list(proper_divisors)