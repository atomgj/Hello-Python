#! /usr/bin/python
foo = open('/usr/local/projects/python/20.txt')
wfoo = open('/usr/local/projects/python/21.txt','w')
while 1:
    b = foo.readline()
    if not b:
        break;
    str = ''
    arr = b.split(',') 
    if(len(arr)==9):  
        for i in arr :
            idx = arr.index(i)
            if(idx==0 or idx==1):
               str+=i+'-'
            elif(idx==3 or idx==4):
               str+=i+':'
            elif(idx!=len(arr)-1):
               str+=i+','
            else:
               str+=i
        print str
        try:
            wfoo.write(str)
	except:
            print str
foo.close()
wfoo.close()  

	

