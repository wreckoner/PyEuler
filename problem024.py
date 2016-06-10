#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer: 2783915460
"""
import math

def enumerate_permutations(lista):
	"""
	Returns all permutations of the elements of lista
	in a sorted order.
	"""
	returns = []
	if len(lista) == 2:
		return [[lista[0], lista[1]], [lista[1], lista[0]]]
	for i in lista:
		permutations = enumerate_permutations([z for z in lista if z != i])
		map(lambda x: returns.append([i]+x), permutations)
	return returns


def brute_force(lista):
	"""
	Good ol' brute force, extremely inefficient!!
	Enumerates all permutations in a lexicographical manner recursively.
	Run time: ~30 sec on i5-5200U 2.20 GHz CPU, 8 Gb Ram.
	"""
	return enumerate_permutations(lista)[999999]

def elegant_method(elements, position, factorial):
	"""
	The most elegant solution which uses permutation theory
	to get the required permutation.
	Runtime: .166 sec in the same environment as the brute force.
	I'll need to think how to describe this solution later!!
	"""
	if position == 0:
		return elements
	remainder = position%factorial
	index = (position-remainder)/factorial
	return [elements[index]] + elegant_method(elements[:index]+elements[index+1:], remainder, factorial/(len(elements)-1))

def main():
	return ''.join(map(str, elegant_method(range(10), 999999, reduce(lambda x,y:x*y, range(1,10)))))

if __name__ == '__main__':
	print main()