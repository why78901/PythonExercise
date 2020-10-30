# -*- coding:utf8 -*-
import urllib
import re
import os
import sys
import shutil
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.pdfgen import canvas

imgurl = sys.argv[1]
pdf_path = sys.argv[2]
file_path = "./img/";
file_suffix = ".png";

if os.path.exists("img"):
	shutil.rmtree("img")
	
os.mkdir("img")

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg1(html):
	reg = 'src="(.+?\.png)" alt='
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	x = 0
	for imgurl in imglist:
		filename = '{}{}{}'.format(file_path,x,file_suffix)
		urllib.urlretrieve(imgurl, filename)
		x+=1
	return imglist

def getImg2(html):
	reg = 'src="(.+?\.jpg)" alt='
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	x = 0
	for imgurl in imglist:
		filename = '{}{}{}'.format(file_path,x,file_suffix)
		urllib.urlretrieve(imgurl, filename)
		x+=1
	return imglist


html = getHtml(imgurl)

print "png list"
print getImg1(html)
print "jpg list"
print getImg2(html)

def convert_images_to_pdf(img_path):
    if(os.path.exists(pdf_path)):
       os.remove(pdf_path);
    pages = 0
    (w, h) = landscape(portrait(A4))
    c = canvas.Canvas(pdf_path, pagesize=landscape(portrait(A4)))
    l = os.listdir(img_path)
	print l
    l.sort(key= lambda x:int(x[:-4]))
    for i in l:
        f = img_path + os.sep + str(i)
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()

convert_images_to_pdf(file_path)