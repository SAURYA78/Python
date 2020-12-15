#!/usr/bin/python
import os
import subprocess
#subprocess.run('free -m' shell=True)

os.system('ls')
print(os.popen('ls').read())

subprocess.call(['ls','-al'])


#input = 'command.py'
#command= "cat {}".format(input)
#subprocess.call('command')
