# 传对象引用
a = [1,2,3,4]
b = a
b[1] = 0
print(a)  #[1, 0, 3, 4]

#传值
a = [1,2,3,4]
b = a[0:2]
b[1] = 0
print(a)  #[1,2,3,4]


#传值
a = [1,2,3,4]
b = a[:]
b[1] = 0
print(a) #[1, 0, 3, 4]
