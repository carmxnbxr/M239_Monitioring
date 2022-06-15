import eel
import psutil
import os

eel.init('web', allowed_extensions=['.js', '.html'])

@eel.expose
def cpuusage():
    result = int(psutil.cpu_percent())
    return result

@eel.expose
def memusage():
    memusage=str(psutil.virtual_memory())
    i=memusage.find("percent=")
    u=memusage.find(", used=")
    i+=8
    u -=2
    result =  memusage[i:u]
    return result 

@eel.expose
def diskusage():
    diskusage=str(psutil.disk_usage('/'))
    i=diskusage.find("percent=")
    i+=8
    result = int(diskusage[i:-3])
    return result 

@eel.expose
def rebootrsp():
    os.system("systemctl reboot")

eel.start('index.html', host='0.0.0.0', mode='firefox', port=80)
