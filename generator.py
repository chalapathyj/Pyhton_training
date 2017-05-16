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

#def create_counter(n):
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

# while True:
#    try:
#       print (next(f), end=" ")
#    except StopIteration:
#       sys.exit()
