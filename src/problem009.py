#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000
"""
import math

def special_pythagorean_triplet(num):
	"""
	n^2 complexity. Let's assume a<b<c. Then for right triangles a<(a+b+c)/3, b<(b+c)/2.
	I came accross an algorith using number theory and euclid's formula to generate the triplets.
	You can search it online if you want.
	"""
	pairs = {}
	for a in xrange(1, int(num/3)):
		for b in xrange(1, int(num-a)/2):
			if math.sqrt(a*a + b*b).is_integer() and (a+b+int(math.sqrt(a*a + b*b))) == num:
				c = int(math.sqrt(a*a + b*b))
				return a*b*c

if __name__ == '__main__':
	print special_pythagorean_triplet(1000)