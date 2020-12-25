#!/usr/bin/python3


import os

file = open("/home/ubuntu/python/file/file1.py", 'r')


print(file.read())  # print content in file

print(file.read(5))   #print first 5 character


#print(file.readline(5)) # print 5th line in a file
#file.close()

