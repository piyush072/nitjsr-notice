import requests
from bs4 import BeautifulSoup
from os import path
import urllib
import os

URL = "http://www.nitjsr.ac.in/allnotice.php"

r = requests.get(URL)

page = r.content
soup = BeautifulSoup(page, features='html5lib')

name = []
link = []

for t in soup.find_all('table',attrs={'class':'table table-striped'}):
    for a in t.find_all('a',href=True):
        name.append(a.text+'\n')
        link.append(a['href'].replace(' ','%20'))

if(path.exists(".notifications.txt")):
    file = open(".notifications.txt", "r")
    x = file.readline()
    for i in range(0,10):
        if(x == name[i]):
            break
    print(i)
st = ""
my_path = '/home/piyush/Downloads/NITJSR_NOTIFICATIONS'
try:
    os.mkdir(my_path)
except FileExistsError:
    pass

for z in range(0,i):
    print('http://www.nitjsr.ac.in/'+link[z].strip())
    urllib.request.urlretrieve('http://www.nitjsr.ac.in/'+link[z],path.join(my_path,name[z].strip()))
    st = st + name[z]

with open('.notifications.txt', 'r') as original: data = original.read()
with open('.notifications.txt', 'w') as modified: modified.write(st + data)
