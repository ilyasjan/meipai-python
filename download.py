# -*- coding: utf-8 -*
#第三方包: bs4,py-term
from bs4 import BeautifulSoup
import urllib2
import term

##  get html content to soup
def getUrlCon(url):
  return BeautifulSoup(urllib2.urlopen(str(url)).read(),"html.parser")

##  get soup
def getUrl(soup):
  div=soup.find(id="detailVideo")
  return str(div.get("data-video"))

##  get mp4 file name
def getFileName(url):
  filename=url[url.rindex('/')+1:len(url)]
  return filename

##  download file
def DownLoad(mediaUrl):
  term.writeLine("--------------------------------------------------------------------------------",term.yellow)
  term.writeLine("开始地址:"+mediaUrl,term.dim)
  url=getUrl(getUrlCon(mediaUrl))
  term.writeLine("文件地址:"+url,term.blue)
  filename=getFileName(url)
  f=open(filename,'wb')
  f.write(urllib2.urlopen(url).read())
  term.writeLine("已下载:"+filename,term.cyan)
  term.writeLine("--------------------------------------------------------------------------------",term.yellow)
  f.close()
  term.write("\n\n\n\n")

##  read file list and download
flist=open('list2.txt','r')
for line in flist.readlines():
    DownLoad(line.strip())
