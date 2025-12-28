import datetime
import time


alarm=input('Alarm with the format %H:%M:%S')
running=True

while running:
    current=datetime.datetime.now().strftime("%H:%M:%S")
    if alarm>current:
        print('wake up')
        break
        running=False
    time.sleep(1)