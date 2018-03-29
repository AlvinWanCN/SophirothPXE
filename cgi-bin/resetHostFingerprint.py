#!/usr/bin/python3
#coding:utf-8
import os,cgi,json,re
print("Content-Type: application/json")
print('')

data=cgi.FieldStorage()
user=data.getvalue('user')
host=data.getvalue('host')
rootfile='/root/.ssh/known_hosts'
alvinfile='/sophiroth/alvin/.ssh/known_hosts'

success = {"success":"True","code":0}
fail = {"success":"False","code":1}
unknown = {"success":"False","code":2}


def processData(user,host):
    global respense
    if user == 'root':
        file='/root/.ssh/known_hosts'
    elif user == 'alvin':
        file='/sophiroth/alvin/.ssh/known_hosts'

    f1=open(file,'r')
    f1Content=f1.read().split('\n')
    f1.close()
    f2=open(file,'w')
    for i in f1Content:
        b=re.sub(r'.*%s.*'%host,'',i)
        if len(b) > 3:
            f2.write(b+'\n')
    f2.close()
    respense = json.dumps(success)

    if user not in ('alvin','root'):
        respense = json.dumps(fail)

processData(user,host)
os.system('''
/usr/bin/expect <<eof
spawn ssh %s
expect {
"yes/no"
{ send "yes\n";exp_continue }
}
expect eof
eof
'''%host)


print(respense)