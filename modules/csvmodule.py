import csv

req_file= "path of file"

fo=open(req_file,"r")

content=fo.readlines()
fo.close()

for each in content:
    print(each.strip('\n'))
