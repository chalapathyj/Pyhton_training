l1 = [1, 2, 3, 4]
op = list(map((lambda x: x ** 2), l1))
print(op)


#passing list of functions to map

# def square(x):
#         return (x**2)
# def cube(x):
#         return (x**3)

# funcs = [square, cube]
# for r in range(5):
#     value = map(lambda x: x(r), funcs)
#     print (list(value))

# passing multiple arugments

#print (list(map(pow, [2, 3, 4], [10, 11, 12])))

#when None is passed instead of a function
# m = [1,2,3]
# n = [5,6,7]
# l2 = map(None, m, n)
# print (list(l2))