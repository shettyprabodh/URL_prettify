#!/usr/bin/python
import re, os, fileinput, shutil, subprocess
from bs4 import BeautifulSoup
from sys import stdout
import time
start_time = time.time()
basepath = os.getcwd()


def check(link, original_f):
	j = -1
	for i in original_f:
		j+=1
		if(i==link):
			return j
	return -2

writ = 1

def check1(csstoreplace, css_files_original):
	j = -1
	for i in css_files_original:
		j+=1
		if(i==csstoreplace):
			return j
	return -2





def ifnotexistadd(string, listtoadd, file_n):
	flag = 0
	for i in listtoadd:
		if(string == i):
			flag=1
			break
	if (flag==0):
		print file_n
		listtoadd.append(string)



#declaring dictionary vairable
original_dict = {}

f = open('original_files.txt', 'r')
original_f = list()
changed_f = list()


for i in range(2417):
	original_f.append(f.readline().replace('\n', ''))
f.close()

f = open('changed_files.txt', 'r')


	
for i in range(2417):
	changed_f.append(f.readline().replace('\n', ''))
f.close()



#making dictionaries
for i in range(2417):
	original_dict[original_f[i]] = changed_f[i]





f = open('iitguwahativirtuallab/error.html','w')

message = """<html>
<title>External Link</title>
<head></head>
<body><p>This link is external</p></body>
</html>"""

f.write(message)
f.close()

print 'writing changes to files.'



for file_n in changed_f:
	if(writ%20==0):
		print '....'
	writ+=1
	soup = BeautifulSoup(open(file_n))
	#
	filetochange =file_n.replace('(','\(')
	filetochange =filetochange.replace(')','\)')
	length = len(file_n)
	for j in range(length-1,0,-1):
		if file_n[j]=='/':
			path_n = file_n[0:j]
			break
	for i in soup.find_all('a'):
		link = str(i.get('href'))
		if(link == 'javascript: authenticate()'):
			path =  basepath+'/iitguwahativirtuallab/error.html'
			relative_path = os.path.relpath(path, path_n)
			relative_path = relative_path.replace('/','\/')
			os.system("sed -i 's/javascript: authenticate()/"+relative_path+"/g' "+filetochange)
		elif(link.startswith('http://')):
			path =  basepath+'/iitguwahativirtuallab/error.html'
			relative_path = os.path.relpath(path, path_n)
			relative_path = relative_path.replace('/','\/')
			linktochange = link.replace('&', '&amp;')
			linktochange = linktochange.replace('/', '\/')
			os.system("sed -i 's/"+linktochange+"/"+relative_path+"/g' "+filetochange)
		else:
			try:
				path = original_dict[link]
			#	print 'try %s'%path
			except KeyError:
				path = basepath+'/iitguwahativirtuallab/error.html'
			#	print 'except %s'%path
			relative_path = os.path.relpath(path, path_n)
			relative_path = relative_path.replace('/','\/')
			linktochange = link.replace('&', '&amp;')
			linktochange = linktochange.replace('/', '\/')
			os.system("sed -i 's/"+linktochange+"/"+relative_path+"/g' "+filetochange)


print("--- %s seconds ---" % (time.time() - start_time))			
				
'''
	for k in soup.find_all('link'):
		linktoreplace =  str(k.get('href'))
		path1 = basepath+'/'+linktoreplace
		print path1
		relative_path = os.path.relpath(path1, path_n)
		relative_path = relative_path.replace('/','\/')
		linktochange = linktoreplace.replace('&', '&amp;')
		linktochange = linktochange.replace('/', '\/')
		os.system("sed -i 's/"+linktochange+"/"+relative_path+"/g' "+filetochange)
		#	csstoreplace = csstoreplace.replace('/', '\/')
		#	os.system("sed -i 's/"+csstoreplace+"/"+relative_path+"/g' "+filetochange)
			
		#else:
		#	print csstoreplace
		#	print 'endswith non css'

#find . -path *.css
'''
