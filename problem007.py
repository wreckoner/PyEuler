# -*- coding: utf-8 -*-
"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Answer: 104743
"""
import math

def prime_seive(upper):
	"""Find all prime numbers upto upper, excluding it. Will throw memory error if the upper bound is too large."""
	lower = 2
	primes = [False] * 2 + [True for x in xrange(lower, upper)]
	for index in xrange(lower, int(math.sqrt(upper))):
		if primes[index]:
			for j in xrange(index*index, upper, index):
				primes[j] = False
	return primes



def main(n):
	""" Find the upper bound of the nth prime number and find all prime numbers upto that bound."""
	upper_bound = int(n*math.log(n)) + int(n*math.log(math.log(n))) # The nth prime number p_n < nlogn +nloglogn #themoreyouknow
	primes = prime_seive(upper_bound+1)
	counter = 0
	for index, is_prime in enumerate(primes):
		if is_prime:
			counter += 1
			if counter == n:
				return index


if __name__ == '__main__':
	print main(10001)