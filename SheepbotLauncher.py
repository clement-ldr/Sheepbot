"""sheepbotlauncher.py
Boot bot and shard
"""
import subprocess
import time
import sys
import json
import signal as signol
import requests
stop = None
Lproc = {}
def signal_handler(signal, frame):
    global stop
    """Intercepte le signal de fermeture !"""
    print('shuting down!')
    stop = True
    for s in shard:
        Lproc.get(s).terminate()
        time.sleep(10)
        Lproc.get(s).kill()
    print('killed shard : '+str(s))
    sys.exit(0)



signol.signal(signol.SIGINT, signal_handler)
shard = range(0, 10)
shardcount = str(10)
for i in shard:
    proc = subprocess.Popen('python3 Sheepbot.py '+str(i)+' '+shardcount, shell=True)
    Lproc[i] = proc

time.sleep(120)
while True:
    if stop:
        break
    try:
        time.sleep(10)
        html = requests.get('http://sheepbot.net:9000/json').text
        html = json.loads(html)
        for s in shard:
            argument = str(s)
            stat = html.get('shard'+str(s))
            if stat.get('good') != 'True':
                proc = Lproc.get(s)
                if proc.poll() != None:
                    print('restarting.'+str(s))
                    proc.terminate()
                    time.sleep(10)
                    proc.kill()
                    proc = subprocess.Popen('python3 Sheepbot.py '+str(i)+' '+shardcount, shell=True)
                    Lproc[s] = proc
                    time.sleep(60)
                else:
                    print('killing'+str(s))
                    proc.terminate()
                    time.sleep(10)
                    proc.kill()
                    print('restarting..'+str(s))
                    proc = subprocess.Popen('python3 Sheepbot.py '+str(i)+' '+shardcount, shell=True)
                    Lproc[s] = proc
                    time.sleep(60)
            else:
                proc = Lproc.get(s)
                if proc.poll() != None:
                    try:
                        print('killing'+str(s))
                        proc.terminate()
                        time.sleep(10)
                        proc.kill()
                    except Exception as e:
                        proc.kill()
                    print('restarting...'+str(s))
                    proc = subprocess.Popen('python3 Sheepbot.py '+str(i)+' '+shardcount, shell=True)
                    Lproc[s] = proc
                    time.sleep(60)
    except Exception as e:
        print('U_u')
