#!/usr/bin/python
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

list = GetFileList('/usr/local/projects/database/20161220', [])
flist = open('/usr/local/projects/database/20161220/files','w')
p = re.compile('txt')
for e in list:
    rs = p.findall(e)
    if len(rs) == 0:
        continue
    str = "'"+e+"','"
    print str
    #flist.write(str);
