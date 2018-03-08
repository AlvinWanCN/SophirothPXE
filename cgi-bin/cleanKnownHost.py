#!/usr/bin/python
#coding:utf-8
import os,cgi,json

data=cgi.FieldStorage()
key=data.getvalue('key')

success = {"success":"True","code":0}
fail = {"success":"False","code":1}

if os.system("sed -i '/%s/d'"%key) == 0:
    respense=json.dumps(success)
else:
    respense = json.dumps(fail)

print("Content-Type: application/json")
print()
print(respense)