#! /usr/bin/python
#coding=utf-8

import re
import os
import time;

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList
    
flist = GetFileList('/usr/local/projects/python/数据', [])
ofile = open('/usr/local/projects/python/'+str(time.time())+'.txt', 'w')
ofile.write('年,月,日,时,分,秒,经度,纬度,强度,站点\r\n')
pattern = re.compile(r'年')
def is_num_by_except(num):
    try:
        float(num)
        return True
    except ValueError:
        #print "%s ValueError" % num
        return False
for fr in flist:
    for line in open(fr, 'r'):
        state = fr.split('/')[6]
        match = pattern.findall(line)
        if len(match) == 0:
            txt = line.split('\r\n')[0]
            s = txt.split(',')
            if len(s) != 9 :
                print s
            else:
                isnum = False
                for i in s:
                    if is_num_by_except(i):
                        isnum = True
                if isnum is True:  
                    s.append(state)
                    str = ','.join(s)+'\r\n'
                    #print str
                    ofile.write(str)
                else:
                    print line
                    print fr
ofile.close()	

