#! /usr/bin/python
foo = open('/usr/local/projects/python/20.txt')
while 1:
    b = foo.readline()
    if not b:
        break;
    str = ''
    arr = b.split(',')
    for i in arr :
        idx = arr.index(i)
        if(idx==0 or idx==1):
           str+=i+'-'
        elif(idx!=len(arr)-1):
           str+=i+','
        else:
           str+=i
    print str
foo.close()

