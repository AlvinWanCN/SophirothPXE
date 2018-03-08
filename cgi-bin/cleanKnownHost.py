#!/usr/bin/python
#coding:utf-8
import os,cgi,json,re

data=cgi.FieldStorage()
user=data.getvalue('user')
host=data.getvalue('host')
rootfile='/root/.ssh/known_hosts'
alvinfile='/sophiroth/alvin/.ssh/known_hosts'

success = {"success":"True","code":0}
fail = {"success":"False","code":1}
unknown = {"success":"False","code":2}

if user == 'root':
    f1=open(rootfile,'r')
    f1Content=f1.read()
    f1.close()
    f2=open(rootfile,'w')
    f2.write(re.sub(r'.*%s.*'%host,'',f1Content))
    f2.close()
    respense=json.dumps(success)
elif user == 'alvin':
    f1=open(alvinfile,'r')
    f1Content=f1.read()
    f1.close()
    f2=open(alvinfile,'w')
    f2.write(re.sub(r'.*%s.*'%host,'',f1Content))
    f2.close()
    respense=json.dumps(success)
else:
    respense = json.dumps(unknown)

print("Content-Type: application/json")
print()
print(respense)
