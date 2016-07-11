#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

Answer: 137846528820
"""
import math

def lattice_paths(grid_dimension):
	""" This problem can easily be solved by combinatorics.
		For an N*N square grid the total number of moves required to reach the bottom right is 2N.
		In addition there will be exactly N moves right and N moves down. What remains is to find the 
		number of ways the moves that has to be made to reach the bottom right from the top left.

		Must admit, I started with a rather stupid way of traversing the state space of all moves!
		"""
	return math.factorial(2 * grid_dimension)/(math.factorial(grid_dimension) * math.factorial(grid_dimension))


if __name__ == '__main__':
	print lattice_paths(20)