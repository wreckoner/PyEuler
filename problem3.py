'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: 6857
'''
import itertools

def main(num):
	prime_factors = []
	for n in itertools.count(2):
		if n > num:
			break
		if num%n == 0:
			prime_factors.append(n)
			while (num%n == 0):
				num = num/n
	return prime_factors


if __name__ == "__main__":
	print max(main(600851475143))