#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
Problem 19: Counting Sundays.

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer: 171
"""

def is_leap(year):
	"""
	Simply returns true or false depending on if it's leap or not.
	"""
	return not year%400 or not (year%4 and year%100)

def counting_sundays():
	"""
	This function simply calculates the cumulative number of days from 1/1/1901 to 1/31/2000, and checks if the 
	cumulative sums are divisible by zero. Note that 1/1/1990 was a Sunday, but I have shifted the day
	number forward by 1, which makes it easy to just check for divisibility by 7.
	This was a pretty challenging and satisfying problem to solve!!
	"""
	sundays = 0
	months_regular = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	first_day_of_month = 0

	for year in xrange(1901, 2001):
		months = months_regular * int(not is_leap(year)) + months_leap * is_leap(year)
		for month in months:
			if first_day_of_month%7 == 0:
				sundays += 1
			first_day_of_month += month

	return sundays



if __name__ == '__main__':
	print counting_sundays()
