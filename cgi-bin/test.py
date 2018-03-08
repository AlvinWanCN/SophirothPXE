#coding:utf-8
import os
print("Content-type:text/html")
print('')
print(os.popen('whoami').read())