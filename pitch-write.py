#! /usr/bin/python
#coding=utf-8

flist = [
'/usr/local/projects/database/20161220/2015/2016_11_17.txt']
ofile = open('/usr/local/projects/python/allinone.txt', 'w')

for fr in flist:
    for txt in open(fr, 'r'):
        try:
            if txt.index('年') :
                print txt
        except:
            ofile.write(txt)
ofile.close()	

