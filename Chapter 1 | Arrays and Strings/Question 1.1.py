#! /usr/bin/env python

# Author: Abhishek Gahlot (c) 2015
# Email: 'me@abhishek.it'


#Implement algorithm to determine if string has all unique characters

#Basic Solution
def hasUniqueChars(_str):
	character_set = set()
	for i in _str:
		if i in character_set:
			return False
		character_set.add(i)
	return True

#Alternate Solution
def hasUniqueChars1(_str):
	if len(set(_str)) != len(_str):
		return False
	return True


print hasUniqueChars1('abcdefghijklmnoqp')



