#! /usr/bin/env python

# Author: Abhishek Gahlot (c) 2015
# Email: 'me@abhishek.it'

#For two strings check if one is permutation of the other.
#Example : god , dog 

#Simple solution using sorting
def permutation(str1,str2):
	return sorted(str1) == sorted(str2)

#Iterative fast solution
def permutation1(str1,str2):
	assert len(str1) == len(str2)
	
	d = {}
	for i in str1:
		if i in d.keys():
			d[i] += 1
		else:
			d[i] = 1
	
	for i in str2:
		if str2.count(i) != d.get(i, 0):
			return False
	return True


print permutation('dog', 'god')

print permutation1('dog', 'god')
