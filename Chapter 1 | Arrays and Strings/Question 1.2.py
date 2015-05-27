#!/usr/bin/python

# Author: Abhishek Gahlot (c) 2015
# Email: 'me@abhishek.it'


#Implement function to reverse a string, Original question is to reverse null string in C/C++

#Simple basic solution
def reverse_str(_str):
	return _str[::-1]

#iterative solution
def reverse_str1(_str):
	new_str = ''
	for i in range(len(_str)-1,-1,-1):
		new_str += _str[i]
	return new_str

#Python inbuilt function
print ''.join(reversed('batman'))

print reverse_str('batman')

print reverse_str1('batman')
