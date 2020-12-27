#!/usr/bin/python3


import re

#text= "this is a python script and it is high programming language"
#my_patt="i[st]"


#my_patt="\w\w"

#my_patt="."



#print(re.findall(my_patt,text))

#text= "This is nmy db server ip: 123.234.231.122 87678678"
#patt= "\d\d\d.\d\d\d.\d\d\d.\d\d\d"

#print(len(re.findall(my_patt,text)))


text = "This about python. Python is eay to learn and we have two major version: python2 and python3"

patt= r'\bpython[23]?\b'

#print(re.findall(patt,text,flags=re.I))
#print(re.search(patt,text))

#print(re.split(text))

########################## PAttern object ****************************

pat_object= re.compile(patt,flags=re.I)

print(pat_object)
print(pat_object.search(text))
print(pat_object.findall(text))
