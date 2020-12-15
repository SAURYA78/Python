#!/usr/bin/python3
import os
import subprocess
subprocess.run("free -m" shell=True)



subprocess.call(['apt', 'install', 'nginx', '-y'])

