#! /usr/bin/python
#coding=utf-8
foo = open('/usr/local/projects/python/20.txt')
wfoo = open('/usr/local/projects/python/30.text','w')
while 1:
    line = foo.readline()
    if not line:
	break
    arr = line.split(',')
    str=''
    for i in arr:
      print i
      idx=arr.index(i)
      if(idx==0 or idx==1):
          str+=i+'-'
      elif(idx==3 or idx==4):
          str+=i+':'
      elif(idx!=len(arr)-1):
          str+=i+','
      else: 
          str+=i
    wfoo.write(str)
foo.close()
wfoo.close()

