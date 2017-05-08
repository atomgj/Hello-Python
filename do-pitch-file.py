#!/usr/bin/python
#coding=utf-8
import os
import re
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('utf-8'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

list = GetFileList('/usr/local/projects/database/20170508', [])
wfile = open('/usr/local/projects/database/20170508/output.txt', 'w')

p = re.compile('txt')

for f in list:
    rs = p.findall(f)

    if len(rs) == 0:
        continue
    for line in open(f, 'r'):
        if not line:
            break
        
        arr = line.split('\r\n')
        str = ''
        print len(arr);
        if len(arr) != 9:
            continue
        for s in arr:
            idx = arr.index(s)
            if idx == 1:
                str += s + ','
            if idx == 2:
                str += s + ','
            if idx == 3 or idx == 4 or idx == 5 or idx == 6 or idx == 7:
                str += s.split('=')[1] + ','
            if idx == 8:
                str += s.split(':')[1]

        print str
        wfile.write(str)
wfile.close()