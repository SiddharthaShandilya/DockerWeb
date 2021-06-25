#! /usr/bin/python3

import cgi
import subprocess

f = cgi.FieldStorage()

docker_cmd = f.getvalue('docker_cmd')

print("content-type: text/html")
print()

output = subprocess.getoutput("sudo " + docker_cmd)

print(output)
