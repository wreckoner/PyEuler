#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
Problem 22: Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Answer: 871198282
"""
import os
def score_word(word):
	"""
	Returns the score of a word.
	"""
	return sum(map(lambda x: ord(x)-ord('a')+1, str(word).lower()))


def names_scores(word_file):
	"""
	Reads file, splits names into list, sorts it and returns the sum
	of the product of word score and postion in list of each name.
	Really simple!
	"""
	_file = open(word_file)
	names = sorted(map(lambda x: x.replace('"', ''), _file.read().split(',')))
	scores = map(lambda x: x[0]*score_word(x[1]), enumerate(names, 1))
	return sum(scores)


if __name__ == '__main__':
	print names_scores(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files', 'p022_names.txt'))
