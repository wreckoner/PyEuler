#/usr/bin/env python
# -*-coding:utf-8 -*-

import unittest
import problem001, problem002, problem003, problem004, problem005, problem006, problem007, problem008, problem009, problem010, problem011, problem012, problem013, problem014, problem015, problem016, problem017, problem018, problem019, problem020, problem021, problem022, problem023

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

	def test_problem_12(self):
		self.assertEqual(problem012.highly_divisible_triangular_number(500), 76576500)

	def test_problem_13(self):
		self.assertEqual(problem013.large_sum(problem013.NUMBER_ARRAY), '5537376230')

	def test_problem_14(self):
		self.assertEqual(problem014.longest_collatz_sequence(1000000), 837799)

	def test_problem_15(self):
		self.assertEqual(problem015.lattice_paths(20), 137846528820)

	def test_problem_16(self):
		self.assertEqual(problem016.power_digit_sum_simple(2, 1000), 1366)
		self.assertEqual(problem016.power_digit_sum_using_list(2, 1000), 1366)

	def test_problem_17(self):
		self.assertEqual(problem017.number_letter_counts(1, 1000), 21124)

	def test_problem_18(self):
		self.assertEqual(problem018.maximum_path_sum_i(problem018.ARRAY), 1074)

	def test_problem_19(self):
		self.assertEqual(problem019.counting_sundays(), 171)

	def test_problem_20(self):
		self.assertEqual(problem020.factorial_digit_sum(100), 648)

	def test_problem_21(self):
		self.assertEqual(problem021.amicable_numbers(10000), 31626)

	# def test_problem_22(self):
	# 	self.assertEqual(problem022.names_scores("./files/p022_names.txt"), 871198282)





if __name__ == '__main__':
	unittest.main()