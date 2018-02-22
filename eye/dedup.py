a = [1,3,5,1,3,4]
b =[]
sum = 0
for x in a:
    if x not in b:
        sum += x
        b.append(x)
    else:
        sum -= x

print (sum)
