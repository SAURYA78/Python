#!/usr/bin/python3


import os



#os.remove("file6")

if os.path.exists("file3"):
    os.remove("file3")
else:
    print("file doesn't exist")

os.rmdir("file6")
