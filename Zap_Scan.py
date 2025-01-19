import requests

from zapv2 import ZAPv2
import time

#The API key of zap
apikey = 'vavd61if8v5f0am57he7jmp6uq' 
zap = ZAPv2(apikey=apikey)


target = input('Enter the target URL: ') #we must chang it 
print(f'Scanning target: {target}')

#proxy
zap.urlopen(target)
time.sleep(2)


#Activ_scan
zap.ascan.scan(target)

while int(zap.ascan.status()) < 100:
    print('Scan progress %: ' + zap.ascan.status())
    time.sleep(5)

print('Scan completed')

alerts = zap.core.alerts(target)
for alert in alerts:
    print('Alert: ' + alert.get('alert'))

