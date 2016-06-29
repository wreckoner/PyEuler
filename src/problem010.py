#-*- coding:utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def main(upper):
	primes = [True if x>1 else False for x in xrange(upper+1)]
	for i in xrange(2, int(math.sqrt(upper+1))):
		if primes[i]:
			for j in xrange(i*i, upper+1, i):
				primes[j] = False
	return sum(i for i, is_prime in enumerate(primes) if is_prime)

if __name__ == '__main__':
	print main(2000000)