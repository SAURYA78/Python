sfile= input("Enter your source file:")
dfile= input("Enter your destination file:")


sfile="/home/ubuntu/Dockerfile"
dfile="/home/ubuntu/dockerfile.txt"


sfo= open(sfile,'r')
content= sfo.read()
sfo.close()

dfo=open(dfile, 'w')
dfo.write(content)
dfo.close()


