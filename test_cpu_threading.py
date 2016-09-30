from threading import Thread 
from time import time

def func(number):
    for i in range(1,number+1):
        if number % i == 0:
            yield i


class MyThread(Thread):
    def __init__(self,number):
        super().__init__()
        self.number = number

    def run(self):
        self.result = list(func(self.number))



numbers = [143454,3423423,345456,4564567]
threads = []

start = time()
for number in numbers:
    threads.append(MyThread(number))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time()

print("multithreading using time: {}".format(end - start))
for thread in threads:
    print(thread.result)



start = time()
for number in numbers:
    print(list(func(number)))
end = time()
print("single threading using time: {}".format(end - start))


