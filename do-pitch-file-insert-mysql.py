#!/usr/bin/python
#coding=utf-8
import os
import re
import time

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

def is_num_by_except(num):
    try:
        float(num)
        return True
    except ValueError:
        print "%s ValueError" % num
        return False
        
list = GetFileList('/usr/local/projects/database/20161220', [])
wfile = open('/usr/local/projects/database/20161220/'+str(time.time())+'.txt', 'w')
wfile.write('序号,年月日,时分秒,纬度,经度,强度,陡度,误差,定位方式,省,市,县\r\n')
log = open('/usr/local/projects/database/20161220/error-'+str(time.time())+'.txt', 'w')
p = re.compile('txt')
i = 0
for f in list:
    rs = p.findall(f)

    if len(rs) == 0:
        continue
    for line in open(f, 'r'):
        if not line:
            break
        uf = ''
        try:
            uf = line.decode('gbk').encode('utf8')
        except:
            try:
                uf = line.decode('utf8').encode('utf8')
            except:
                print line
                print f
        arr = uf.split('\r\n')[0].split()
        isnum = False
        newArr = []
        for s in arr:
            try:
                idx = arr.index(s)
                if idx == 1 or idx == 2:
                    newArr.append(s)
                elif idx == 3 or idx == 4 or idx == 5 or idx == 6 or idx == 7:
                    val = s.split('=')[1]
                    if is_num_by_except(val):
                        isnum = True
                    newArr.append(val)
                elif idx == 8 or idx == 9 or idx == 10 or idx == 11:
                    try:
                        loc = s.split(':')[1]
                    except:
                        try: 
                            loc = s.split('：')[1]
                        except:
                            loc = ''
                    newArr.append(loc)
            except:
                print arr
                log.write(line)
        if isnum is True:
            i = i + 1
            alen = len(newArr)
            if alen == 7:
                newArr.append('')
            elif alen == 8:
                newArr.append('')
                newArr.append('')
                newArr.append('')
            string = str(i)+',' + ','.join(newArr)+'\r\n'
            wfile.write(string)
wfile.close()