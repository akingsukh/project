#!/usr/bin/python

#import urllib2 
import sys
from HTMLParser import HTMLParser  

class MyHTMLParser(HTMLParser):
 def __init__(self):
   	HTMLParser.__init__(self)
	self.inlink = False
	self.dataArray = []
	self.lasttag = None

 
 def handle_starttag(self, tag, attrs):
    self.inlink = False
    if tag.lower() == "p":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "div":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "b":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "i":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "td":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "h1":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "h2":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "h3":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "h4":
	self.inlink = True
	self.lasttag = tag
    elif tag.lower() == "h5":
	self.inlink == True
	self.lasttag = tag
    elif tag.lower() == "span":
	self.inlink = True
	self.lasttag = tag
        
 def handle_endtag(self, tag):
	if tag == "p":
		self.inlink = False
	elif tag == "div":
		self.inlink = False
	elif tag == "b":
		self.inlink = False
	elif tag == "i":
		self.inlink = False
	elif tag == "td":
		self.inlink = False
	elif tag == "h1":
		self.inlink = False
	elif tag == "h2":
		self.inlink = False
	elif tag == "h3":
		self.inlink = False
	elif tag == "h4":
		self.inlink = False
	elif tag == "h5":
		self.inlink = False
	elif tag == "span":
		self.inlink = False

 def handle_data(self, data): 
      	if self.lasttag == 'p'or 'div' or 'b' or 'i' or 'td' or 'h1' or 'h2' or 'h3' or 'h4' or 'h5' or 'span':
	   if self.inlink == True and data.strip():
               str1 = self.lasttag + " = " + data.strip() + "\n"
	       fout = open('example.properties', 'a')
	       fout.write(str1)
 
p = MyHTMLParser()
file_name = sys.argv[1]
fp = open(file_name)
html = fp.read()
p.feed(html)
p.close()
