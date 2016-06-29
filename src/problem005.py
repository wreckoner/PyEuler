"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer: 232792560
"""

def problem_5(upper):
	"""
	This method returns the smallest multiple of all the integes less than or equal to <upper>.
	It has an upper bound of x^2 on the time complexity. 
	"""
	numbers = range(upper+1)
	lcm = 1	#lowest common multiple.
	for index, number in enumerate(numbers):
		if index <= 1:
			continue
		else:
			for j in xrange(index+1, upper+1):
				if numbers[j]%number == 0:
					numbers[j] /= number
			lcm *= number
	return lcm


if __name__ == "__main__":
	print problem_5(20)