#!/usr/bin/python3


import sys
import os


os.chdir("/home/ubuntu")
print(os.getcwd())

os.mkdir("/home/ubuntu")

os.rmdir("/home/ubuntu")

print(os.path.join("home/ubuntu/folder1", "home/ubuntu/folder1/file1.py"))

print(os.path.exists("home/ubuntu/folder1", "home/ubuntu/folder1/file1.py"))


