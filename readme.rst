
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
    git clone https://github.com/AlvinWanCN/sophiroth-pxe.git


Startup
`````````````````````

 需要用拥有sudo权限的非root用户执行，因为如果是root用户执行的，则实际cgi user会变成nobody，用非root用户，如alvin，则cgi的user就是alvin，可以拥有sudo权限。

.. code-block:: bash

    echo '
    [Unit]
    Description=The Sophiroth Service
    After=syslog.target network.target salt-master.service

    [Service]
    Type=simple
    User=alvin
    WorkingDirectory=/opt/sophiroth-pxe
    ExecStart=/usr/bin/python3 -m http.server --cgi 8001
    KillMode=process
    Restart=on-failure
    RestartSec=3s


    [Install]
    WantedBy=multi-user.target graphic.target
    ' > /usr/lib/systemd/system/sophiroth-pxe.service
    systemctl enable sophiroth-pxe
    systemctl start sopihroth-pxe
    systemctl status sophiroth-pxe
    lsof -i:8001


这里我们是指定了端口为tcp 8001端口

shutdown
`````````````````````

.. code-block:: bash

    systemctl stop sophiroth-pxe
