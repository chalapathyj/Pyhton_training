#simple loop
s = [x for x in range(10)]
print (s)

#applying condition similar to map
s1 = [x*2 for x in range(5)]
print (s1)
#applying condition and setting delimiter (both map and filter)

s2 = [x**2 for x in range(10) if x % 2 != 0]
print (s2)

#nested for loops
s3 = [x+y for x in 'apple' for y in 'orange']
print (s3)

#nested for loops with if conditions
s4 = [x+y for x in range(6,11) if x % 2 ==0 for y in range (5) if y %2  != 0]
print (s4)