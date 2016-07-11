#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
Problem 14: Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer: 837799
"""
import math

def longest_collatz_sequence(upper_bound=1000000):
	"""
	This calculates the length of all collatz sequence with starting number between 1 and 1 million.
	There are 2 optimizations:
		1. If a number is a power of 2, then no need to calculate further
		2. Caches the length of collatz sequences, so if larger sequence contain a smaller one, simply adds the length.
	"""
	longest = 0
	cached = {}
	for init_val in xrange(1, upper_bound):
		val, length = init_val, 0
		while val > 1:
			if math.log(val, 2).is_integer():
				length += (int(math.log(val, 2)) + 1)
				break
			elif val in cached:
				length += cached[val]
				break
			elif val%2 == 0:
				val = val/2
				length += 1
			else:
				val = 3*val + 1
				length += 1
		cached[init_val] = length
		if longest < length:
			start = init_val
			longest = length
	return start

if __name__ == '__main__':
	print longest_collatz_sequence(1000000)