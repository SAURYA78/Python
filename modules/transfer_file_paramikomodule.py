#!/usr/bin/python3


import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # It required permission like yes or no as an standard input
ssh.connect(hostname='123.0.1.201',username='ubuntu',key_filename='mumbai_region.pem',port=22)


sftp_client=ssh.open_sftp()


sftp_client.chdir("/home/ubuntu/")
print(sftp_client.getcwd())
sftp_client.get('/home/ubuntu/python/modules/osmodule.py', '/home/ubuntu')

#transfer one file from one server to another server

sftp_client.put('/home/ubuntu/python/modules/osmodule.py', '/home/ubuntu')
sftp_client.close()

ssh.close()
