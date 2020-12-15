import shutil

#copy, copy2, copyfile, copyfileobj, copymode, copystat, copytree

src= "/home/ubuntu/python/command.py"
dest= "/home/ubuntu/python/command.py.bkp"

#shutil.copyfile(src,dest)  # permission is changed
#shutil.copy(src,dest)     # --> permission is preserved means permission is not changed during copy

#shutil.copy2(src,dest)   # no any permission is changed/ same metadata for dest like timestamp

#shutil.copymode(src,dest)  # only permission is changed to any other file 

#shutil.copystat(src,dest)  #permission with timestamp u can assign to other file without copying content



#f1= open('src.txt', 'r')
#f2= open('dest.txt', 'w')
#shutil.copyfileobj(src,dest)


#shutil.copytree(src,dest)    # it copies all files and dir under src file 


#shutil.rmtree('dest')

