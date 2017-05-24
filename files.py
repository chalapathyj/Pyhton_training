f = open('foo.txt', 'r')
data = f.read()
print (data)

import os
import time
print(os.getcwd())
print(os.path.join('/test/', '/myfile'))
pathname = "/Users/K/dir/subdir/k.py"
print (os.path.split(pathname))
import glob
print(glob.glob('/home/runner/*.py'))
metadata = os.stat('file2.py')
print ("file size:", metadata.st_size)
print ("file modified:", time.asctime(time.localtime(metadata.st_mtime)))

import re

with open('foo.txt', 'a') as file:
	file.write('\n added  6th line through append mode')
	
with open('foo.txt', encoding='utf-8') as file:
    for line in file:
        #srch = re.search('(5th)',line)
        #sub1 = re.sub('This','It',line, 1)
        print('{:<1}'.format(line.rstrip()))
        #if srch:
          #print (srch.group(1))
