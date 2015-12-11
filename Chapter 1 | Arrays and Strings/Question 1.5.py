#! /usr/bin/env python

# Author: Abhishek Gahlot (c) 2015
# Email: 'me@abhishek.it'

#Compress string

def compress_string(string):
  tmp = string[0]
  count = 1
  compressed = ""
  for i in string[1:]:
    if tmp == i:
      count += 1
    else:
      compressed += tmp + str(count)
      tmp = i
      count = 1
  compressed += tmp + str(count)
  return compressed if len(string) > len(compressed) else string
     
print compress_string("abcd")

print compress_string("aabbbbcccdaaddd")
      
      
    