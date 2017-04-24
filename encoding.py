#! /usr/bin/python
#coding: utf-8
foo = open('/usr/local/projects/database/2007_01_25.txt')
while 1:
    b = foo.readline()
    if not b:
        break;
    print b.decode('gbk').encode('utf8')
foo.close()
