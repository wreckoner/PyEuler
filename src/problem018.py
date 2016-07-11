#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Problem 18: Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

Answer: 1074
"""

import pprint

ARRAY = [
			[75],
			[95, 64],
			[17, 47, 82],
			[18, 35, 87, 10],
			[20, 04, 82, 47, 65],
			[19, 01, 23, 75, 03, 34],
			[88, 02, 77, 73, 07, 63, 67],
			[99, 65, 04, 28, 06, 16, 70, 92],
			[41, 41, 26, 56, 83, 40, 80, 70, 33],
			[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
			[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
			[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
			[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
			[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
			[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
			]

def maximum_path_sum_i(array):
	""" 
	I'll admit I started thinking of a tree traversal algorithm, before reading up on the internet,
	and found this approach. Deceptively simple!
	Essentially, goes bottom-up from the second last row, and at each row finds the bigger adjacent number in the next row and replaces the current number by the sum of itself and the bigger number.
	You can check out this post on SO: http://stackoverflow.com/questions/8002252/euler-project-18-approach
	"""
	while len(array) > 1:
		for i in xrange(len(array[-2])):
			array[-2][i] += max(array[-1][i], array[-1][i+1])
		array.pop(-1)
	return array[0][0]

if __name__ == '__main__':
	print main(ARRAY)