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

def simple_way(num=100):
	"""
	This method simply calculates the factorial and then returns the sum of the digits.
	This method would not work in many languages which have a maximum limit for integral numbers.
	"""
	fact = 1
	for i in xrange(1, 101):
		fact *= i

	_sum = 0
	while fact > 0:
		_sum += fact%10
		fact /= 10
	return _sum

def multiply_list_by_number(multiplicand, multiplier):
	carry = 0
	pass 


def using_list(num=100):
	"""
	This method computes the factorial using a list, storing each digit in each index. 
	"""
	fact = []
	pass


if __name__ == '__main__':
	print simple_way()