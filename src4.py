from os import walk
from bs4 import BeautifulSoup
import os
import re
fname = []
dirpath = []
big =0
file = "index.html"
qlinks_php = []
qlinks = []
link_encode = {}
for (dirpath, dirnames, filenames) in walk(os.path.dirname(os.path.abspath(__file__))):
    	fname.extend(filenames)
	#dirpath.extend(dirpath)
    	break
for filename in fname:
	num = []
	num = re.findall("\d+", filename)
	if(big<=len(num)):
		big = len(num)
	#if(len(num) == 0):
	#	print (filename)
print (big)
soup = BeautifulSoup(open("index.html"))
link = [l.get('href') for l in soup.find_all('a') if 'sub' in l.get('href')]
qlinks.append(link)
for m in link:
        str1 = ""
        num = []
        num = re.findall(r'\d+',m)
        for k in num:
                str1 = str1 + k + "."
        str1 = str1 + ".html"
        link_encode[m] = str1
        print (link_encode[m])


soup = BeautifulSoup(open("index.php.html"))
link_php = [l.get('href') for l in soup.find_all('a') if 'sub' in l.get('href')]
qlinks_php.append(link_php)
for m in link_php:
        str1 = ""
        num = []
        num = re.findall(r'\d+',m)
        for k in num:
                str1 = "php" + "." + str1 + k + "."
        str1 = str1 + ".html"
        link_encode[m] = str1
        print (link_encode[m])
#print (qlinks)
#os.mkdir(os.getcwd() + soup.title.name)
#os.rename(os.getcwd(),soup.title)
#print (qlinks)
#for i in range(big+1)
        
        #for link in soup.find_all('a'):
         #       if('sub' in link.get('href')):
          #          print(link.get('href'))
print (link_encode)
#print (qlinks[0])
while len(qlinks)>0:          
        for (links,links_php) in zip(qlinks[0],qlinks_php[0]):
                if (os.path.exists(links) == False):
                        links = link_encode[links]
                if (os.path.exists(links_php) == False):
                        links_php = link_encode[links_php]
                str1 = ""
                str1_php = ""
                str2 = ""
                str2_php = ""
                num = []
                num = re.findall(r'\d+',links)
                num_php = []
                num_php = re.findall(r'\d+',links_php)
                if(len(links) != 0):
                        soup = BeautifulSoup(open(links,encoding="cp850"))
                else:
                        break
                pass
                if(len(links_php) != 0):
                        soup_php = BeautifulSoup(open(links_php,encoding="cp850"))
                else:
                        break
                pass
                #os.mkdir(os.getcwd() + soup.title.string)
                for k in num:
                        str1 = str1 + k + "."
                str2 = str1 + ".html"
                #print (soup.title.string)
                for k in num_php:
                        str1_php = str1_php + k + "."
                str2_php = "php." + str1_php + ".html"
                #print (soup.title.string)
                print (links)
                print (links_php)
                if(len(num) == 1):
                        os.makedirs(str1)
                        os.rename(links,str2)
                        os.rename(links_php,str2_php)
                        link_encode[links] = str2
                        link_encode[links_php] = str2_php
                        #pass
                elif(len(num) == 2):
                        os.makedirs(num[0] + "\\" + str1)
                        os.rename(links,num[0] + "\\" + str2)
                        os.rename(links_php,num[0] + "\\" + str2_php)
                        link_encode[links] = num[0] + "\\" + str2
                        link_encode[links_php] = num[0] + "\\" + str2_php
                elif(len(num) == 3):
                        os.makedirs(num[0] + "\\" + num[0] + "." + num[1] + "\\" +str1)
                        os.rename(links,num[0] + "\\" + num[0] + "." + num[1] + "\\" + str2)
                        os.rename(links_php,num[0] + "\\" + num[0] + "." + num[1] + "\\" + str2_php)
                        link_encode[links] = num[0] + "\\" + num[0] + "." + num[1] + "\\" + str2
                        link_encode[links_php] = num[0] + "\\" + num[0] + "." + num[1] + "\\" + str2_php
                elif(len(num) == 4):
                        os.makedirs(num[0] + "\\" + num[0] + "." + num[1] + "\\" + num[0] + "." + num[1] + "." + num[2] + "\\" +str1)
                        os.rename(links, num[0] + "\\" + num[0] + "." + num[1] + "\\" + num[0] + "." + num[1] + "." + num[2] + "\\" +str2)
                        os.rename(links_php, num[0] + "\\" + num[0] + "." + num[1] + "\\" + num[0] + "." + num[1] + "." + num[2] + "\\" +str2_php)
                        link_encode[links] = num[0] + "\\" + num[0] + "." + num[1] + "\\" + num[0] + "." + num[1] + "." + num[2] + "\\" + str2
                        link_encode[links_php] = num[0] + "\\" + num[0] + "." + num[1] + "\\" + num[0] + "." + num[1] + "." + num[2] + "\\" + str2_php        
                #os.rename(links,str1)
                #link_encode[links] = str2
                #os.rename(os.getcwd(),soup.title)
                link1 = [l.get('href') for l in soup.find_all('a') if l.get('href') != None and 'sub' in l.get('href') and l.get('href') not in link_encode and 'http' not in l.get('href') and '#' not in l.get('href') and 'php' not in l.get('href')]
                qlinks.append(link1)
                #print (link_encode)
                #print (qlinks)
                link1_php = [l.get('href') for l in soup_php.find_all('a') if l.get('href') != None and 'sub' in l.get('href') and l.get('href') not in link_encode and 'http' not in l.get('href') and '#' not in l.get('href') and 'php' in l.get('href')]
                qlinks_php.append(link1_php)
        del qlinks[0]
        del qlinks_php[0]
        #print (qlinks[0])
        
        
print ((qlinks))
print ((qlinks_php))
#print (link_encode)
#print (link_encode)

#----------------Rename-------------------

for key in link_encode:
    f_rename = open(link_encode[key])
    soup_rename = BeautifulSoup(f_rename)
    for link_rename in soup_rename.find_all('a'):
        os.system("sed -i 's/" + link_rename + "/" + link_encode[link_rename] + "/g' " + link_encode[key])
