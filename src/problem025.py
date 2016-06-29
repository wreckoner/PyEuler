#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Problem 25: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Answer: 4782
"""

def number_of_digits(number):
	"""
	Returns the number of digits of @number.
	"""
	digits = 0
	while number > 0:
		digits += 1
		number /= 10
	return digits


def fibonacci(digits):
	"""
	Returns the position of the first number with
	number of digits = @digits in the fibonacci sequence.
	"""
	i = 2
	i_1 = i_2 = 1
	fib = 0
	while number_of_digits(fib) < digits:
		fib = i_1 + i_2
		i += 1
		i_2 = i_1
		i_1 = fib
	return i


if __name__ == '__main__':
	print fibonacci(1000)
	