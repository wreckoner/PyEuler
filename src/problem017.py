#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Problem 17:	Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters 
used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer:	21124
"""

def number_letter_counts(lower_bound=1, upper_bound=1000):
	"""
	The numbers with having basic (not composed of other number-words) words are saved in a dict and then a nested if else checks each number according to the naming rules for numbers. Self-explanatory. 
	"""
	number_to_word = {
		0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
		12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 
		20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 1000: 'one thousand'
	}
	length = 0
	for num in xrange(lower_bound, upper_bound+1):
		if num <= 20:
			word = number_to_word[num]
		elif num < 100:
			if num%10 == 0: # Multiples of 10
				word = number_to_word[num]
			else:
				word = ' '.join([number_to_word[num/10*10], number_to_word[num%10]])
		elif num < 1000:
			if num%100 == 0: # Multiples of 100
				word = ' '.join([number_to_word[num/100], 'hundred'])
			elif num%100 in number_to_word: # Numbers whose last two digits are in the dict.
				word = ' '.join([number_to_word[num/100], 'hundred and', number_to_word[num%100]])
			else:
				word = ' '.join([number_to_word[num/100], 'hundred and', number_to_word[num%100/10*10], number_to_word[num%10]])
		else:
			word = number_to_word[num]				

		length += len(word.replace(' ', ''))
	return length


if __name__ == '__main__':
	print number_letter_counts(1, 1000)