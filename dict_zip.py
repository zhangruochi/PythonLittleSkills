a = {"zhang":1,"ruo":2,"chi":3}
b = {"zhang":4,"xiao":5,"yue":6}

print(min(zip(a.values(),a.keys())))

#字典元素排序

for item in sorted(zip(b.values(),b.keys())):
    print(item)



for item in sorted(b.items(),key = lambda x:x[1]):
    print(item)


#在字典中找相同的元素

c = a.keys() & b.keys()
print(c) 
c = a.keys() - b.keys()
print(c)