#!D:/python-3.6.2/python.exe 
print ("Content-Type: text/html\n")
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',user='root',password='',db='pymysql',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print ("connect successful!!")

def decodeWebPage(base_url):
	import requests
	from bs4 import BeautifulSoup
	#base_url=input('Enter Url(ex. http://www.nytimes.com): ')
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text)	
	for story_heading in soup.find_all(class_= {'story-heading','default','title'}):
		if story_heading.a:
			print(story_heading.a.text.replace("\n"," ").strip())
		else:
			print (story_heading.content[0].strip())
			
print (decodeWebPage('http://www.nytimes.com'))
			
## >>> decodeWebPage()
## Enter Url(ex. http://www.nytimes.com): http://bangla.bdnews24.com
## >>> decodeWebPage()
## Enter Url(ex. http://www.nytimes.com): http://www.prothom-alo.com

