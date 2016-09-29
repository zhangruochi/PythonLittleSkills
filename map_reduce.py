import os
from threading import Thread

class InputData: 
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):   #生成文件对象
    def __init__(self,path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path,"r").read() 

 
class Worker:
    def __init__(self,input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

class LineCountWorker(Worker):  #生成工人对象
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self,other):
        self.result += other.result



def generates_input():  #每个文件都生成文件对象
    for file in os.listdir("PythonLittleSkills"):
        yield PathInputData(os.path.join("PythonLittleSkills",file))

def create_workers(input_list):  #利用文件对象生成工人对象
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

def execute(workers):    #多线程执行
    threads = [Thread(target = worker.map) for worker in workers]
    for thread in threads: 
        thread.start()
    for thread in threads:
        thread.join()

    first,rest = workers[0],workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result    

def mapreduce():
    input_list = generates_input()
    workers = create_workers(input_list)
    result = execute(workers)
    print(result)








if __name__ == '__main__':
    mapreduce()    








