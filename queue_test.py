#encoding:utf-8
from threading import Thread, current_thread
import random
import time
from queue import Queue

queue = Queue(5)


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 休眠了 %s 秒' % (name, t))


class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()#队列为空时被挂起
            print('消费者 %s 消耗了数据 %s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 休眠了 %s 秒' % (name, t))


p1 = ProducerThread(name='p1')
p1.start()
p1 = ProducerThread(name='p1')
p1.start()
c1 = ConsumerThread(name='c1')
c1.start()
c1 = ConsumerThread(name='c1')
c1.start()
c1 = ConsumerThread(name='c1')
c1.start()