#!/usr/bin/env python
# *-*coding:utf-8 -*-

"""
Problem 26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Answer: 983

"""

def get_recurrence_length(d):
	"""
	Gets the recurrence length of 1 divided by integer d.
	It does this by keeping track of remainders obtained by continuous division by d
	and the first time a remainder occurs more than once, it is the end of recurrence since the previous occurence of the remainder.
	"""
	remainders = {}
	remainder = 10
	for i in xrange(1, 100000):
		# print i, remainders
		if remainder < d:
			remainder *= 10
			continue
		elif remainder%d == 0:
			return 0
		else:
			remainder %= d
			if remainder in remainders:
				return i - remainders[remainder]
			else:
				remainders[remainder] = i
				remainder *= 10
	else:
		return 0



def reciprocal_cycles(upper_limit):
	"""
	Returns the number less than upper_limit which when
	dividing 1 produces a number with largest recurrence.
	"""
	max_len, max_d = 0, 1
	for d in xrange(2, upper_limit):
		rec_len = get_recurrence_length(d)
		if rec_len and rec_len > max_len:
			max_d = d
			max_len = rec_len
	return max_d


if __name__ == '__main__':
	print reciprocal_cycles(1000)
	
