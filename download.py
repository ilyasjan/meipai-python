from bs4 import BeautifulSoup
import urllib2
import os

##  get html content to soup
def getUrlCon(url):
  return BeautifulSoup(urllib2.urlopen(url).read(),"html.parser")

##  get soup
def getUrl(soup):
  div=soup.find(id="detailVideo")
  return str(div.get("data-video"))

##  get mp4 file name
def getFileName(url):
  return url[url.rindex('/')+1:len(url)]

##  download file
def DownLoad(mediaUrl):
  url=getUrl(getUrlCon(mediaUrl))
  filename=getFileName(url)
  f=open(filename,'wb')
  f.write(urllib2.urlopen(url).read())
  f.close()

##  read file list and download
flist=open('list.txt','r')
for line in flist.readlines():
    DownLoad(line)
