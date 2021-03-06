# -*- coding:utf-8 -*-

"""
Problem 12: Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Answer: 76576500 (12375 th divisor)
"""

import math


def highly_divisible_triangular_number(num):
	"""
	Simple brute force, keeps generating triangle numbers, calculates all divisors and finds their count till more than 500.
	"""
	n = 1
	divisors = {1:1, 2:2}
	while True:
		triangle_number = (n * (n+1))/2
		divisors = []
		for i in xrange(1, int(math.ceil(math.sqrt(triangle_number)))):
			if triangle_number%i == 0:
				divisors.extend([i, triangle_number/i])
		if len(divisors) > num:
			return triangle_number
		n += 1

if __name__ == '__main__':
	print highly_divisible_triangular_number(500)