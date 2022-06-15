<h1>M239 Monitioring Tutorial </h1>


<h3>Voraussetungen: </h3>
Debian Server mit Root rechten


<h3>Installation von Updates: </h3>

```
apt-get update && apt-get upgrade -y
```


<h3>Installation von Python 3.8.4 and pip </h3>

```
sudo apt install libffi-dev libbz2-dev liblzma-dev libsqlite3-dev libncurses5-dev libgdbm-dev zlib1g-dev libreadline-dev libssl-dev tk-dev build-essential libncursesw5-dev libc6-dev openssl git -y
```

```
cd /root
wget https://www.python.org/ftp/python/3.8.4/Python-3.8.4.tar.xz
tar xf Python-3.8.4.tar.xz
```

```
cd Python-3.8.4
./configure
make -j -l 4
make altinstall
echo "alias python=python3.8" >> ~/.bashrc
echo "alias pip3=pip3.8" >> ~/.bashrc
source ~/.bashrc
```
<h3>Install eel </h3>

```
pip3 install eel
```

<h3>Install Python Module psutil </h3>
```
pip3 install psutil
```

```
mkdir /monitor
cd /monitor
wget <Link>
```

```
python3.8 /monitor/start.py
```

<h3>Webseite über Browser aufrufen</h3>
Connect to IP (Befehl: ip a) / localhost

Zu Autostart hinzufügen

```
nano /etc/systemd/system/monitor.service
```

```
[Unit]
Description=Monitoring Web Server

[Install]
WantedBy=multi-user.target

[Service]
ExecStart=/bin/sh /monitor/autostart.sh
Type=simple
User=root
```

```
systemctl enable monitor.service
systemctl start monitor.service
```
