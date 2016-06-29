'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: 6857
'''
import itertools

def problem_3(num):
	"""
	Largest prime factor of num.
	"""
	prime_factors = []
	for n in itertools.count(2):
		if n > num:
			break
		if num%n == 0:
			prime_factors.append(n)
			while (num%n == 0):
				num = num/n
	return max(prime_factors)


if __name__ == "__main__":
	print(problem_3(600851475143))