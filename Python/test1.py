#coding = utf-8
import os
import time
from multiprocessing import Process 

def func(name, num, **kwargs):
    print("Child process")
    print(name)
    print(num)

    for k,v in kwargs.items():
        print("%s:%s"%(k,v))
    
#p = Process(target=func, name="process1", args=("test", 10,), kwargs={"name":"jack", "age":10})
p = Process(target=func, name="p1", args=("test",10), kwargs={"name":"jack", "age":10})
p.start()
p.join()
