# -*- coding: cp936 -*-
import urllib2
import imghdr
import os
#connect to a URL
f1 = open("pic.txt")
line = f1.readline()
n=1
while line:
    n=n+1
    print 'No.'+str(n)
    line=line.strip('\n')
    url= str(line)
    url2 = url.replace(" ", "%20")
    imgname=url.rsplit('/', 1)[-1]
    if os.path.exists('c:\\pic\\{}'.format(imgname)):
        print str(n)+' '+imgname+' ok\n'
    else:
        try:
            upen = urllib2.urlopen(url2 ,timeout=10)
            content =upen.read()
            imgtype = imghdr.what('', h=content)
            with open('D:\\pic\\{}'.format(imgname), 'wb') as f:
                f.write(content)
                print str(n)+' getPic '+imgname+'\n'
        except:
            print 'error'
    line = f1.readline()
a=raw_input()
f1.close()
