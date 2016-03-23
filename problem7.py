# -*- coding: utf-8 -*-
"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
Answer: 
"""
import math

def main(n):
	estimate = int(n*math.log(n))
	primes = [True if x >1 else False for x in xrange(estimate+1)]
	# print primes
	for index, _ in enumerate(primes):
		if index < 2:
			continue
		elif primes[index]:
			for j in xrange(index, int(math.sqrt(estimate+1)), index):
				primes[index] = False
	return estimate


if __name__ == '__main__':
	print main(10001)
