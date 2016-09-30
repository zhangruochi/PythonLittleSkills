from threading import Thread
from threading import Lock
from multiprocessing.dummy import Pool as ThreadPool

class Counter:
    def __init__(self):
        self.count = 0

    @property
    def increment(self):
        self.count += 1   
                

class Worker:
    def __call__(self,counter,how_many):
        for _ in range(how_many):
            counter.increment

def run_threads():
    how_many = 10**5
    counter = Counter()
    threads = []
    worker = Worker()
    for i in range(5):
        thread = Thread(target = worker, args = (counter,how_many))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("true output is: 5000000, but the real output is: {}".format(counter.count)) 



#-------------lock--------------------


class LockCounter:
    def __init__(self):
        self.lock = Lock() 
        self.count = 0

    @property
    def increment(self):
        with self.lock:
            self.count += 1


def run_threads_withlock():
    how_many = 10**5
    counter = LockCounter()
    threads = []
    pool = ThreadPool(5)
    worker = Worker()
    for i in range(10):
        pool.apply_async(func = worker,args = (counter,how_many))
    
    pool.close()
    pool.join()
    print("true output is: 1000000, but the real output is: {}".format(counter.count))    




if __name__ == '__main__':
    run_threads() 
    run_threads_withlock()          


