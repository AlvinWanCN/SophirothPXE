#!/usr/bin/python
#coding:utf-8
import subprocess,cgi,hashlib,json
print("Content-Type: application/json")
print('')


try:
    hl = hashlib.md5()
    data=cgi.FieldStorage()
    ip=data.getvalue('ip')
    hostname=data.getvalue('hostname')
    hl.update(data.getvalue('password').encode(encoding='utf-8'))
    password=hl.hexdigest()
    dns_server='dns.alv.pub'
    file='/var/named/alv.pub.zone'
except Exception as e:
    print(json.dumps({'code':2,'message':str(e)}))
if  password == '20a2495a46e8d2aa6600dec33501326f':
    if ip and hostname:
        subprocess.call("""sudo salt 'dns.alv.pub' cmd.run 'sed -i "/%s/d" %s'"""%(hostname,file),shell=True)
        subprocess.call("""sudo salt 'dns.alv.pub' cmd.run 'echo %s A %s >> %s'"""%(hostname,ip,file),shell=True)
        subprocess.call("""sudo salt 'dns.alv.pub' cmd.run 'systemctl restart named'""",shell=True)
        print(json.dumps({'code': 0, 'message': 'success'}))
    else:
        print(json.dumps({'code': 1, 'message': 'ip and hostname cannot null.'}))
else:
    print(json.dumps({'code':2,'message':'Password error'}))



