#!/usr/bin/python3
import os
import subprocess
subprocess.run("free -m" shell=True)



subprocess.call(['apt', 'install', 'nginx', '-y'])




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
