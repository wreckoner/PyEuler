#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
Problem 21: Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
"""

import math, _lib


def amicable_numbers(limit):
	"""
	Iterates through all the numbers from 2  through limit and saves the sum of proper divisors of 
	each number in a hashtable. In a second iteration, finds all amicable paris.
	"""
	sum_of_divisors = {}
	for num in xrange(2, limit+1):
		proper_divisors = _lib.get_proper_divisors(num)
		sum_of_divisors[num] = sum(proper_divisors)

	sum_amicable_numbers = 0
	for num in sum_of_divisors:
		if num == sum_of_divisors.get(sum_of_divisors[num]) and num!=sum_of_divisors[num]:
			sum_amicable_numbers += num

	return sum_amicable_numbers


if __name__ == '__main__':
	print(amicable_numbers(10000))