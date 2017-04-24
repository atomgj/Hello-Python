#! /usr/bin/python
foo = open('/usr/local/projects/python/20.txt')
while 1:
    b = foo.readline()
    if not b:
        break;
    print b
foo.close()
