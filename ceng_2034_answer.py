#!/usr/bin/python3

import os
import sys
import threading
import requests
import time
#import psutil


print("\n")
print("pID : " + str(os.getpid()))
print("\n")
print("LoadAvg : " + str(os.getloadavg()))
#print("LoadAvg : " + str(psutil.getloadavg()))

#int1 = psutil.getloadavg()
int1 = os.getloadavg()
int2 = int1[1]
FiveMinLoadAvg = "5 min.loadavg: " + str(int2)
print(FiveMinLoadAvg)

print("\n")

print("cpu count : " + str(os.cpu_count()))

print("\n")



array = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
'https://www.python.org/', 'http://akrepnalan.com/ceng2034', 'https://github.com/caesarsalad/wow']


def status(array):

        r = requests.head(array)
        httpcode = str(r.status_code)
        print(array + "\n" + "   <response: " + httpcode + "> " + "\n")




start = time.time()

thread1 = threading.Thread(target=status, args=(array[0],))
thread2 = threading.Thread(target=status, args=(array[1],))
thread3 = threading.Thread(target=status, args=(array[2],))
thread4 = threading.Thread(target=status, args=(array[3],))
thread5 = threading.Thread(target=status, args=(array[4],))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

finish = time.time()
print("\n" + "elapsed time: " + str(finish - start) + "\n")





result1 = "'cpu count - 5 min. loadavg' "
result2 = os.cpu_count() - int2

if result2 >= 1:
    print(result1 + "=  " + str(result2))
else:
    print(result1 + "=  " + str(result2)) & sys.exit("\n 'cpu count - 5 min. loadavg' < 1 \n")