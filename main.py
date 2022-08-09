#This python code converts any Amazon India website(amazon.in) link to an affiliate link and also shortens it.
#Library used: pyshorteners


import pyshorteners

#Taking the URL as an input
url = input('Enter the url: ')
#Adding my Amazon Associate ID to the amazon.in URL
url = url + '?tag=prakharkati00-21'


#Shortening the amazon.in URL, with the tag ingluded
def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)