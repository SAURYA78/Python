#!/usr/bin/python3


import os

file = open("/home/ubuntu/python/file/file6", 'a')

file.write("again hello \n ")
file.write("hello world saurav \n ")



#file.write("Hi world")

file = open("/home/ubuntu/python/file/file6", 'r')

print(file.read())
