#coding:utf-8
import subprocess,cgi
print("Content-type:text/html")
print('')

data=cgi.FieldStorage()
password=data.getvalue('pw')

if   password != 'sophiroth':
    print('wrong authentication.')
    exit(2)

if str(subprocess.call('sudo salt-key -A  -y',shell=True)) == '0':
    print('success')
else:
    print('possible have wrong')
