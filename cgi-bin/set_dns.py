#!/usr/bin/python
#coding:utf-8
import subprocess,cgi,hashlib,json
print("Content-Type: application/json")
print('')

hl = hashlib.md5()
data=cgi.FieldStorage()
ip=data.getvalue('ip')
hostname=data.getvalue('hostname')
password=hl.update(data.getvalue('password').encode(encoding='utf-8'))
dns_server='dns.alv.pub'

if  password == 'a006971e8a57f1cff1a44de29a9314f5':
    if ip and hostname:
        subprocess.call("""sudo salt 'dns.alv.pub' cmd.run 'sed "/diana/d" /root/alv.pub.zone'""",shell=True)
        subprocess.call("""sudo salt 'dns.alv.pub' cmd.run 'echo %s A %s >> /root/alv.pub.zone'""",shell=True)
        subprocess.call("""sudo salt 'dns.alv.pub' cmd.run 'systemctl restart named'""",shell=True)
    else:
        print(json.dump({'code': 1, 'message': 'ip and hostname cannot null.'}))
else:
    print(json.dump({'code':2,'message':'Password error'}))


