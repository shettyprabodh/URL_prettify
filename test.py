import os
from bs4 import BeautifulSoup
import fileinput
link = []
link1 = []
f = open("index.html","r+b")
soup = BeautifulSoup(f)
#print (soup.title.string)
print (soup.find_all('a'))
tag = soup.a
type(tag)
tag['href'] = "6.html"
#if(len(soup.find_all('a')) != 0):
link = [l.get('href') for l in soup.find_all('a') if l.get('href') != None and 'sub' in l.get('href')]
for i in link:
    print (i)
#print (os.path.relpath("index.html@sub=59&brch=163&sim=264&cnt=1046.html"))
for qwe in soup.find_all('a'):
	#if soup.find_all('a') in qwe:
	#		f.write(qwe.replace(,"58\\58.160..html"))
	#qwe['href'] = "58\\58.160..html"
	#href = qwe.get('href')
	#k = qwe.text + ".html"
	#h = os.path.join()
	href = qwe.get('href')
	new = "58\\58.160..html"
	#qwe.get('href') = new

link1 = [l.get('href') for l in soup.find_all('a') if l.get('href') != None]
for i in link1:
    print (i)

print (link1)
