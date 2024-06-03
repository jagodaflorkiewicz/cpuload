import time
import psutil
for n in range(1000):
    print(psutil.cpu_percent(percpu=True))
    time.sleep(1)

