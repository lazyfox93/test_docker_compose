import requests
import subprocess
import time
 

def check_available_nod():
    print("start check")
    timeout = time.time() + 60
    while True:
        if time.time() > timeout:
            status = False
            break
        try:
            resp = requests.get(url="http://172.18.0.2:4444/grid/api/hub/").json()
        except requests.exceptions.RequestException:
            continue
        else:
            if resp['slotCounts']['total'] >= 1:
                status = True
                break
    print("finish check")
    return status

if check_available_nod():
     subprocess.call(['python3', 'run_test.py'])
else:
    print("FAILED")

