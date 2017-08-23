# -*- coding: cp936 -*-
import urllib2
import imghdr
#connect to a URL
f1 = open("pic.txt")             # pic.txt == per picture's urls saved per line eg:http://www.example.com/pic.jpg
line = f1.readline()             #  readline() == read picture url per line

while line: 
    line=line.strip('\n')
    url= str(line)
    content = urllib2.urlopen(url).read()
    imgtype = imghdr.what('', h=content)
    imgname=url.rsplit('/', 1)[-1]      # imgname == picture name eg:pic.jpg
    with open('F:\\Download\\pic\\{}'.format(imgname), 'wb') as f:   #download dir
        f.write(content)
        print 'get pic '+imgname+'successfully \n'
    line = f1.readline()
a=raw_input() #pause
f1.close()
