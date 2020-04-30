import time
import os
while 1:
    times=1588243200-int(time.time())
    print('now ,gohome :{}/s'.format(times))
    time.sleep(1)
    a=0 if times==0 else 1
    if a==0:
        os.system("shutdown now")
