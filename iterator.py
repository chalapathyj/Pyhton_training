list1 = [1,2,3,4,5,6,7]
it = list1.__iter__()
print (next(it))
print (next(it))

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for x in Counter(3,8):
    print (x)
