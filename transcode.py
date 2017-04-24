#! /usr/bin/python
import os
import re

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

list = GetFileList('/usr/local/projects/database/20161220', [])
p = re.compile('txt')
for f in list:
    rs = p.findall(f)
    if len(rs) == 0:
        continue
    for line in open(f, 'r'):
        if not line:
            break
        print line.decode('gbk').encode('utf8')