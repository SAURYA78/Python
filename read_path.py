import os
import subprocess
import sys
path= input(" Enter your path:- ")
if os.path.exists(path):
    df_l= os.listdir(path)
else:
    print("please provide valid path")
    sys.exit()

list_all_files_dir = os.listdir(path)

for each_file_or_dir in list_all_files_dir:
    f_d_p = os.path.join(path,each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f"{each_file_or_dir} is a file")
    else:
        print(f"{each_file_or_dir} is a directory")






'''

p1=os.path.join(path,df_l[0])
p2=os.path.join(path,df_l[1])

if os.path.isfile(p1):
    print(f"{p1} is a file")
else:
    print(f"{p1} is a directory")


if os.path.isfile(p2):
    print(f"{p2} is a file")
else:
    print(f"{p2} is a directory")

#subprocess.call('ls')

'''
