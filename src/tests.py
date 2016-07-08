#/usr/bin/env python
# -*-coding:utf-8 -*-

import unittest
import problem001, problem002, problem003, problem004, problem005, problem006, problem007, problem008, problem009, problem010, problem011

class Test_Problems(unittest.TestCase):

	def test_problem_1(self):
		self.assertEqual(problem001.multiples_of_3_and_5(1000), 233168)
		
	def test_problem_2(self):
		self.assertEqual(problem002.even_fibonacci_numbers(4000000), 4613732)

	def test_problem_3(self):
		self.assertEqual(problem003.largets_prime_factor(600851475143), 6857)

	def test_problem_4(self):
		self.assertEqual(problem004.largest_palindrome_product(), 906609)

	def test_problem_5(self):
		self.assertEqual(problem005.smallest_multiple(20), 232792560)

	def test_problem_6(self):
		self.assertEqual(problem006.sum_square_difference(100), 25164150)

	def test_problem_7(self):
		self.assertEqual(problem007._10001st_prime(10001), 104743)

	def test_problem_8(self):
		self.assertEqual(problem008.largest_product_in_a_series(problem008.SERIES), 23514624000)

	def test_problem_9(self):
		self.assertEqual(problem009.special_pythagorean_triplet(1000), 31875000)

	def test_problem_10(self):
		self.assertEqual(problem010.summation_of_primes(2000000), 142913828922)

	def test_problem_11(self):
		self.assertEqual(problem011.largest_product_in_a_grid(problem011.GRID), 70600674)


if __name__ == '__main__':
	unittest.main()