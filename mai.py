#!/usr/bin/python
# coding = utf-8
foo = open('/usr/local/projects/database/mai.txt')
ofile = open('/usr/local/projects/database/mai-obj.txt', 'w')
while 1:
    b = foo.readline()
    if not b:
        break;
    arr = b.split("	")
    str = '"'+arr[2].strip()+'": {"page":"'+arr[0]+'", "action" : "'+arr[1]+'-'+arr[2].strip()+'"},'+"\n"
    print str
    ofile.write(str);
    
foo.close()
