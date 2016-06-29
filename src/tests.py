#/usr/bin/env python
# -*-coding:utf-8 -*-

import unittest
import problem001, problem002, problem003, problem004, problem005, problem006, problem007,problem007, problem008, problem009, problem010, problem011, problem012

class Test_Problems(unittest.TestCase):

	def test_problem_1(self):
		self.assertEqual(problem001.problem_1(1000), 233168)
		
	def test_problem_2(self):
		self.assertEqual(problem002.problem_2(4000000), 4613732)

	def test_problem_3(self):
		self.assertEqual(problem003.problem_3(600851475143), 6857)

	def test_problem_4(self):
		self.assertEqual(problem004.problem_4(), 906609)

	def test_problem_5(self):
		self.assertEqual(problem005.problem_5(20), 232792560)

	def test_problem_6(self):
		self.assertEqual(problem006.problem_6(100), 25164150)

	def test_problem_7(self):
		self.assertEqual(problem007.problem_7(10001), 104743)


if __name__ == '__main__':
	unittest.main()