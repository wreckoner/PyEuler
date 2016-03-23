'''
Problem 4

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

def main():
	upper, lower = 999, 100
	largest = 0
	for a in xrange(upper, lower, -1):
		for b in xrange(a, lower, -1):
			if is_palindrome(a*b) and largest < a*b:
				largest = a*b
	return largest

if __name__ == "__main__":
	print main()