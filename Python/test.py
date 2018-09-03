import os
import multiprocessing
from multiprocessing import Process
import time
for item in [(a, b) for a in range(1, 10) for b in range(1, 10) if a+b==8]:
    #time.sleep(1)
    print(item)


