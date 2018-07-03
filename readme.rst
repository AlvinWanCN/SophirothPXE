
Sophiroth PXE System.
################################

.. contents::


Requirements
```````````````````

python3
-----------
Install python3

.. code-block:: bash

    python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/python/instrallpython3.6.5.py)"


Install sophiroth pxe
```````````````````````````

.. code-block:: bash

    cd /opt/
    git clone https://github.com/AlvinWanCN/SophirothPXE.git


启动服务的方式
`````````````````````

 需要用拥有sudo权限的非root用户执行，因为如果是root用户执行的，则实际cgi user会变成nobody，用非root用户，如alvin，则cgi的user就是alvin，可以拥有sudo权限。


    cd SophirothPXE
    nohup /usr/bin/python3 -m http.server --cgi 8001 & >/tmp/8001.log &

这里我们是指定了端口为tcp 8001端口，日志文件是/tmp/8001.log


开机自动启动
````````````````

.. code-block:: bash

    # cat /etc/rc.local
    su alvin -c "curl -s https://raw.githubusercontent.com/AlvinWanCN/sophiroth-cluster/master/saltstack.alv.pub/scripts/startup_sophirothpxe.py|python"