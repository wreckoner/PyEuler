#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer: 4179871
"""
import math

def get_proper_divisors(number):
	"""
	Returns a tuple of proper divisors of number.
	"""
	if number == 1:
		return ()
	proper_divisors = set([1])
	for i in xrange(2, int(math.sqrt(number))+1):
		if number%i == 0:
			proper_divisors.add(i)
			proper_divisors.add(number/i)
	return tuple(proper_divisors)

def get_abundant_numbers(upper=28123):
	"""
	Returns a set of all abundant numbers less than upper.
	"""
	abundant_numbers = set([])
	for i in xrange(12, upper+1):
		proper_divisors = get_proper_divisors(i)
		if sum(proper_divisors) > i:
			abundant_numbers.add(i)
	return abundant_numbers

def main(upper=28123):
	"""
	Good ol' brute force. Create a hashset of all abundant numbers,
	then find all numbers less than upper which cannot be a sum of
	any two abundant numbers.
	"""
	answer = 0
	abundant_numbers = get_abundant_numbers(upper)
	for num in xrange(1, upper+1):
		for n in abundant_numbers:
			if num-n in abundant_numbers:
				break
		else:
			answer += num
	return answer

if __name__ == '__main__':
	print main()