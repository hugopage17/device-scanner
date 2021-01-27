from pythonping import ping
import sys
import webbrowser
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
import subprocess

def poll(host):
    response = ping(host, size=32, timeout=1, count=1)
    res = str(response._responses[0])
    return res

def getNext(host):
    newHost = host.split('.')[3]
    newHost = int(newHost)-1
    ip = host.replace(host.split('.')[3], str(newHost))
    return ip

host = input('IP Address: ')
foundNode = False

while foundNode == False:
    res = poll(host)
    if res == 'Request timed out':
        print(host+' unresponsive')
        host = getNext(host)
        poll(host)
    else:
        print(host+' online')
        try:
            requests.get(url='https://'+host, verify=False, timeout=1)
            foundNode = True
            webbrowser.open('http://'+host)
        except:
            subprocess.call('O:\Suppliers_&_Manuals\Winbox\winbox.exe')
        break
