#! /usr/bin/python
foo = open('/usr/local/projects/python/all.txt')
wfoo = open('/usr/local/projects/python/allinone.txt','w')
while 1:
    b = foo.readline()
    if not b:
        break;
    print b
    if b!='<U+FEFF>':
      wfoo.write(b)
foo.close()
wfoo.close()
