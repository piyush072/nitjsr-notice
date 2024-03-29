#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from os import path
import urllib
import os
import subprocess as s

URL = "http://www.nitjsr.ac.in/allnotice.php"

r = requests.get(URL)

page = r.content
soup = BeautifulSoup(page, features='html5lib')

name = []
link = []

cwd = os.path.dirname(os.path.realpath(__file__))

for t in soup.find_all('table',attrs={'class':'table table-striped'}):
    for a in t.find_all('a',href=True):
        name.append(a.text+'\n')
        link.append(a['href'].replace(' ','%20'))

if(path.exists(os.path.join(cwd,".notice.txt"))):
    file = open(os.path.join(cwd,".notice.txt"), "r")
    x = file.readline()
    for i in range(0,10):
        if(x == name[i]):
            break
st = ""
my_path = '/home/username/Downloads/NITJSR_NOTICES' #add your own username
try:
    os.mkdir(my_path)
except FileExistsError:
    pass

for z in range(0,i):
    s.call(['notify-send','New Notification',name[z].strip()])
    urllib.request.urlretrieve('http://www.nitjsr.ac.in/'+link[z],path.join(my_path,name[z].strip()))
    st = st + name[z]

with open(os.path.join(cwd,".notice.txt"), 'r') as original: data = original.read()
with open(os.path.join(cwd,".notice.txt"), 'w') as modified: modified.write(st + data)
