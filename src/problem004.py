'''
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
'''
def is_palindrome(num):
	""" Returns true if a number is a palindrome """
	reverse, forward = 0, num
	while (num > 0):
		reverse = reverse*10 + num%10
		num /= 10
	return forward == reverse

def largest_palindrome_product():
	"""Enumerate all 6 digit palindromes 999*999 downwards, and inspect each palindrome for a 3 digit factor."""
	upper, lower = 999, 100
	for i in xrange(upper**2, lower**2, -1):
		if is_palindrome(i):
			factor = upper
			while factor >= lower:
				if i%factor == 0 and lower-1<(i/factor)<upper+1 :
					return i
				else:
					factor -= 1


if __name__ == "__main__":
	print largest_palindrome_product()