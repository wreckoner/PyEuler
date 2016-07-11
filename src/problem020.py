#!/usr/bin/python
# -*-coding:utf-8 -*-

"""
Problem 20: Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer: 648
"""

def factorial_digit_sum(num):
	"""
	This method simply calculates the factorial and then returns the sum of the digits.
	This method would not work in many languages which have a maximum limit for integral numbers.
	"""
	fact = reduce(lambda x,y: x*y, xrange(1, 101))
	_sum = reduce(lambda x,y:x+int(y), str(fact), 0)
	return _sum


if __name__ == '__main__':
	print factorial_digit_sum(100)
