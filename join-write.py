#! /usr/bin/python
#coding=utf-8
foo = open('/usr/local/projects/database//范围内闪击文件.txt')
wfoo = open('/usr/local/projects/database/范围内闪击.txt','w')
while 1:
    b = foo.readline()
    if not b:
        break;
    str = ''
    arr = []
    arr = b.split(',') 
    if(len(arr)==9):  
        str = arr[0]+'-'+arr[1]+'-'+arr[2]+','+arr[0]+','+arr[1]+','+arr[2]+','+arr[3]+','+arr[4]+','+arr[5]+','+arr[6]+','+arr[7]+','+arr[8];
        print str
        try:
            wfoo.write(str)
	except:
            print str
foo.close()
wfoo.close()  

	

