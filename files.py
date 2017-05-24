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
