#!/usr/bin/python3
#coding:utf-8
import os,cgi,json,sys

data=cgi.FieldStorage()
user=data.getvalue('user')
host=data.getvalue('host')


success = {"success":"True","code":0}
fail = {"success":"False","code":1}
unknown = {"success":"False","code":2}
if user == 'root':
    if os.system("sudo sed -i '/%s/d' /root/.ssh/known_hosts"%host) == 0:
        respense=json.dumps(success)
    else:
        respense = json.dumps(fail)
elif user == 'alvin':
    if os.system("sed -i '/%s/d' /sophiroth/alvin/.ssh/known_hosts"%host) == 0:
        respense=json.dumps(success)
    else:
        respense = json.dumps(fail)
else:
    respense = json.dumps(unknown)

os.system('rpm -q expect &>/dev/null|| sudo yum install expect -y &>/dev/null')



#print("Content-Type: application/json")
#print('')
#print(respense)



print("Content-type:text/html")
print('')
print(os.popen('whoami').read())