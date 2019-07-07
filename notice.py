from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver") #change path here

URL = "http://www.nitjsr.ac.in/allnotice.php"
browser.get(URL)

page = browser.page_source
soup = BeautifulSoup(page, features='lxml')

for td in soup.find_all('td',attrs={'class':'fsize foo'}):
    for a in td.find_all('a',attrs={'class':'fsize foo'}):
        print(a.text)

browser.close()
