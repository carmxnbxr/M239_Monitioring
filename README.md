<h1>M239 Monitioring Tutorial </h1>


<h3>Voraussetungen: </h3>
Debian Server mit Root rechten
Als root auf dem Server einloggen

<h3>Installation von Updates: </h3>

```
apt-get update && apt-get upgrade -y
```


<h3>Installation von Python 3.8.4 and pip </h3>

```
apt install libffi-dev libbz2-dev liblzma-dev libsqlite3-dev libncurses5-dev libgdbm-dev zlib1g-dev libreadline-dev libssl-dev tk-dev build-essential libncursesw5-dev libc6-dev openssl git unzip -y
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

<h3>Install eel Webserver & Python Module </h3>

```
pip3 install eel
pip3 install psutil
```
<h3>Download Application Files</h3>

```
cd /root
wget "https://github.com/carmxnbxr/M239_Monitioring/archive/refs/heads/main.zip"
unzip main.zip
mkdir /monitor
cp ./M239_Monitioring-main/sources/* /monitor -R
rm main.zip
rm M239_Monitioring-main -r
cd /monitor
```

<h3>Start Web Server</h3>

```
python3.8 /monitor/start.py
```

<h3>Webseite über Browser aufrufen</h3>
IP-Adresse (mit "ip a" abfragen) oder localhost (Auf dem Gerät)

<h2>Zu Autostart hinzufügen</h2>

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

<1>Anpassungen</h1>

<h2>Hintergrund wechseln</h2>

```
cd /monitor/web/img
```
Das Bild "background.jpg" austauschen.


<h2>Farben der Kreise ändern</h2>

```
cd /monitor/web/css
nano circle.css
```
Die Hex-Werte der Farben ändern <br>
![image](https://user-images.githubusercontent.com/60874453/173820834-2f2e3db2-2081-4f92-aaaf-159e419619cf.png)
