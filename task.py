#!/usr/bin/python
# coding = utf-8
foo = open('/usr/local/projects/database/task')
ofile = open('/usr/local/projects/database/task.txt', 'w')
while 1:
    b = foo.readline()
    if not b:
        break;
    arr = b.split("	")
    if len(arr) > 4:
        str = arr[1].strip()+arr[2].strip()+arr[4].strip()+"\n"
        print str
        ofile.write(str);
    
foo.close()
