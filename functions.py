# local scope
#global scope
# external scope


# def func1(a, b):
#     print("values passed to the funciton are %d, %d" % (a, b))
#     print("address of a and b are", id(a), id(b))
#     a = 100
#     b = 200
#     print("Address after the change", id(a), id(b))
#     return (a, b)

# a = 10
# b = 20
# print("Address of the variables a and b before passing:", id(a), id(b))
# a, b = func1(a, b)
# print("Return value of a is %d and b is %d" %(a,b))


# default value
# def defvalue(x=10, y=20):
# 	return x+y, x-y

# a,b = defvalue()
# print ("no args a value: %d" %a)
# print ("no args b value: %d" %b)

# a,b = defvalue(a)
# print ("one arg a value: %d" %a)
# print ("one arg b value: %d" %b)

# a,b = defvalue(a, b)
# print ("2 args a value: %d" %a)
# print ("2 args b value: %d" %b)

#for k, name in enumerate(dir(__builtins__)):
#	print (name)


# for k, v in globals().items():
#     print (k, "=", v)

# lambda functions:
#version difference
#inp1 = raw_input("Enter a value: ")
#print (inp1 + 3)


# def writer():
#     title = 'Sir'
#     #name = 'new'
#     name = (lambda x: title + ' ' + x)
#     return name

# who = writer()
# print(who('Arthur Ignatius Conan Doyle'))
