'''
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(num):
	reverse, forward = 0, num
	while (num > 0):
		reverse = reverse*10 + num%10
		num /= 10
	return forward == reverse

def main():
	maximum = 999 * 999
	while maximum > 100 * 100:
		maximum -= 1
		if is_palindrome(maximum):
			return is_product(maximum)
	return False

if __name__ == "__main__":
	main()