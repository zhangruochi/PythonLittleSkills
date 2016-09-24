#-*- coding:utf8 -*-
class A(object):  
    def foo(self,x):  
    #类实例方法  
        print "executing foo(%s,%s)"%(self,x)  
 
    @classmethod  
    def class_foo(cls,x):  
    #类方法  
        print "executing class_foo(%s,%s)"%(cls,x)  
 
    @staticmethod  
    def static_foo(x):  
    #静态方法  
        print "executing static_foo(%s)"%x  


a = A()  
a.foo(1)    
  
a.class_foo(1)    
A.class_foo(1)      
  
a.static_foo(1)    
A.static_foo(1)   