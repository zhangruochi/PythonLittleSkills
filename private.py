class Test2:
    def __init__(self):
        self.a = 10
    def print_a(self):
        print (self.a)    

a = Test2()
print (a.a) 
a.print_a()  


#私有变量 加单个下划线
#私有成员 加两个下划线
class Test:
    def __init__(self):
        self._a = 10
    def __print_a(self):
        print(self._a)    

b = Test()
b._print_a()
 


