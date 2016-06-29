# -*- coding: utf-8 -*-
"""
Problem 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150
"""

def main(lim):
	sum_of_squares = 0
	summation = 0

	for i in  xrange(1, lim+1):
		sum_of_squares += i*i
		summation += i

	return abs(sum_of_squares - summation*summation)

if __name__ == '__main__':
	print(main(100))