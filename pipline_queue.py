from queue import Queue  
from threading import Thread
#Queue 线程安全  当队列中没有任务时  get()方法会一直阻塞  同事可以定义队列的最大容量
#将任务分为各种不同的阶段 每一阶段用不同的线程执行




def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item


class ClosableQueue(Queue):
    SENTINEL  = object()

    def close(self):
        self.put(self.__class__.SENTINEL)

    
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.__class__.SENTINEL:
                    return  #使得线程停止
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self,func,in_queue,out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)




download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for i in range(1000):
    download_queue.put(object())

download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')    




