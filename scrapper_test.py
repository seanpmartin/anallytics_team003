import sys
import os
import urllib2
import re

def main(argv):
    #scrap the web
    #connect to fake news
    website = urllib2.urlopen('http://nytimes.com/')
    w = urllib2.urlopen('https://www.ncbi.nlm.nih.gov/')
    #read html code
    html = w.read()
    #use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://.*?)"',html)
    link1, link2 = zip(*links)
    print link1
    print link2
    print lsd

if __name__ == "__main__":
    main(sys.argv[0:])
