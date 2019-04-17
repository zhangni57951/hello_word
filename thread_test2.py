# import threading
# from threading import current_thread
#
# class Mythread(threading.Thread):
#     def run(self):
#         print(current_thread().getName())
#
#
# t1 = Mythread()
# t1.run()
# t1.start()


import threading
import time
from threading import current_thread

def myThread(arg1, arg2):
    print(current_thread().getName()+'_start')
    print('%s %s'%(arg1, arg2))
    time.sleep(1)
    print(current_thread().getName()+'_stop')
    time.sleep(1)

for i in range(1,6,1):
    t=threading.Thread(target=myThread, args=(i, i+1))
    t.start()
t.join()
print(current_thread().getName()+'_end')