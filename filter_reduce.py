l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f1 = list(filter((lambda x: x > 5), l1))
print(f1)

a = [1, 2, 2, 2, 3, 4, 5]
b = [6, 7, 9, 2, 3, 1]
print(list(filter(lambda x: x in a, b)))

from functools import reduce
l2 = []
# L = ['Testing ', 'shows ', 'the ', 'presence',
#      ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
f2 = reduce((lambda x, y: x+y ), l2)
#f2 = reduce((lambda x, y: x+y ), l2, 'Empty value')
print (f2)
