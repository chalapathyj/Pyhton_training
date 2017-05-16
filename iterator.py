# def samp(n):
# 	n += 2
# 	print ("Inside the function")
# 	return n

# c = samp(5)
# print (c)

# def genfunc(num):
#     print("Inside the generator")
#     while True:
#         num += 1
#         yield num
#         print("Generator continues from where it stopped.")
#         yield (num * 2)
#         print("Encountered 2nd yield operation")
#         #return 1
# f = genfunc(10)
# #g = genfunc(20)
# print(f)

# print(next(f))
# #print (next(g))
# print(next(f))
# try:
# 	print(next(f))
# except:
# 	pass
# print(next(f))


# def sqrs(n):
# 	for i in range(n):
# 		yield i ** 2 # return i ** 2

# for i in sqrs(5):
# 	print(i,  end=',')

# def create_counter(n):
# 	print('create_counter()')
# 	while True:
# 		yield n
# 		print('increment n')
# 		n += 1


# import sys
# def fibonacci(n): #generator function
#    a, b, counter = 0, 1, 0
#    while True:
#       if (counter > n):
#          return
#       yield a
#       a, b = b, a + b
#       counter += 1
# f = fibonacci(5) #f is iterator object
# #f1 = list(f)
# #print (f1)
# while True:
#    try:
#       print (next(f), end=" ")
#    except StopIteration:
#       sys.exit()

# Generator Expressions:
# List comprehension makes a list
#print ([ x ** 3 for x in range(5)])
#[0, 1, 8, 27, 64]

# Generator expression makes an iterable
#print (x ** 3 for x in range(5))
#<generator object <genexpr> at 0x000000000315F678>

# def repeat5times(x):
# 	for c in x:
# 		yield c * 5
# G = repeat5times('python')
# print (next(G))
# print (next(G))
# L = [1, 2, 3, 4]
# I1, I2 = iter(L), iter(L)
