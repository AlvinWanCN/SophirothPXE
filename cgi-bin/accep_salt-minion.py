#!/usr/bin/python
#coding:utf-8
import subprocess
print("Content-type:text/html")
print('')

if str(subprocess.call('sudo salt-key -A  -y',shell=True)) == '0':
    print('success')
else:
    print('possible have wrong')
