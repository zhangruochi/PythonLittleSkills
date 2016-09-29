class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self,path):
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls,config):  #具体的GenericInputData子类可以解读字典
        datadir = config['data_dir']
        for name in os.listdir(data_dir):
            yield clc(os.path.join(data_dir,name))



class GenericWorker(object):
    def __init__(self,input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls,input_class,config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self,other):
        self.result += other.result
            

def mapreduce(worker_class,input_class,config):
    workers = worker_class.create_workers(input_class,config)
    return execute(workers)


 


