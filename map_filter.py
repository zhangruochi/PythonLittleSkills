a = list(range(1,10))
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#列表推导
result = [x ** 2 for x in a if x%2 != 0]
print(result) #[1, 9, 25, 49, 81]

#map and filter
result = list(map(lambda x:x ** 2,filter(lambda x:x%2 != 0,a)))
print(result) #[1, 9, 25, 49, 81]
