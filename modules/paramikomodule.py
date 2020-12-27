#!/usr/bin/python3


import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # It required permission like yes or no as an standard input
ssh.connect(hostname='123.0.1.201',username='ubuntu',key_filename='mumbai_region.pem',port=22)

stdin,stdout,stderr = ssh.exec_command('free -m')

print("The output is: ")
print(stdout.readlines())

print("The error is: ")
print(stderr.readlines())




#print(stdout.read())
