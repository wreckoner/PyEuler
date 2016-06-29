#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Problem 16:	Power digit sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

Answer:	1366
"""
import math

def simple_way(base=2, power=1000):
	"""Simply finds the power using Python's math.pow. Note that a lot of languages do not support such large numbers."""
	result = int(math.pow(base, power))
	summation = 0
	while result > 0:
		summation += result%10
		result /= 10
	return summation


def using_list(base=2, power=1000):
	"""
	This method stores the number as a list, each digit as a separate element. 
	This overcomes any limit that may exist on the max size of number datatype.
	"""
	result = [1]
	for i in xrange(power):
		carry = 0
		for index in xrange(len(result)-1, -1, -1):
			product = result[index]*base
			result[index] = (product + carry)%10
			carry = (product + carry)/10
		if carry > 0:
			result = map(int, list(str(carry))) + result
	return sum(result)


if __name__ == '__main__':
	print simple_way(2, 1000)
	print using_list(2, 1000)
