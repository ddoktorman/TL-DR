#!/usr/bin/python
print "Content-type:text/html\n"
import cgitb
import cgi
from google import search
from bs4 import BeautifulSoup
import requests
cgitb.enable()

data = cgi.FieldStorage()

book = data["book"].value

shmoopurl = ""
sparkurl = ""

urls =[]
for url in search(book, stop = 10): #searches for requested book, and returns top 10 urls
    urls.append(url)
for item in urls:
    if "shmoop" in item: #checks for a link to shmoop, and only shmoop
        shmoopurl += item
        break
if not shmoopurl:
    for item in urls:
        if "sparknotes" in item: #checks for a link to sparknotes if no shmoop link is found
            sparkurl += item
            break

if "summary.html" in shmoopurl:
    shmoopurl = shmoopurl.replace('summary.html', '')
if "summary.html" in sparkurl:
    sparkurl = sparkurl.replace('summary.html', '')

def summarize():
    text = ""
    if shmoopurl:
        page = requests.get(shmoopurl + "summary.html")
        soup = BeautifulSoup(page.content, 'lxml')
        descript = BeautifulSoup(str(soup.find(class_ = 'content-learning-guide')), 'lxml')
        title = descript.find('h1')
        par = descript.find_all('p')
        text += "<h1>" + title.getText() + "</h1>"
        i = 0
        while i < len(par) - 4:
            text += par[i].getText()
            i += 1
        while "\n" in text:
            text = text.replace('\n', '<br>')
    elif sparkurl:
        page = requests.get(sparkurl + "summary.html")
        soup = BeautifulSoup(page.content, 'lxml')
        char = BeautifulSoup(str(soup.find(class_='studyGuideText')), 'lxml')
        ads = char.find_all(class_= 'floatingad')
        strads = []
        text = char.getText()
        for ad in ads:
            strads.append(BeautifulSoup(str(ad), 'lxml').getText())
        for ad in strads:
            text = text.replace(ad, '')
        while '\n' in text:
            text = text.replace('\n', '<br>')
    return text
    
def characterize():
    text = ""
    if shmoopurl:
        page = requests.get(shmoopurl + "characters.html")
        soup = BeautifulSoup(page.content, 'lxml')
        char = BeautifulSoup(str(soup.find(class_ = 'btn-color-cycle-long')),'lxml')
        links = char.find_all('a')
        urls = []
        for link in links:
            x = BeautifulSoup(str(link), 'lxml')
            tag = x.a
            urls.append(tag['href'])
        for url in urls:
            page = requests.get(shmoopurl + url)
            soup = BeautifulSoup(page.content, 'lxml')
            descript = BeautifulSoup(str(soup.find(class_ = 'content-learning-guide')), 'lxml')
            title = descript.find('h1')
            par = descript.find_all('p')
            text += "<h1>" + title.getText() + "</h1>"
            i = 0
            while i < len(par) - 4:
                text += par[i].getText()
                i += 1
            while "\n" in text:
                text = text.replace('\n', '<br>')
    elif sparkurl:
        page = requests.get(sparkurl + "canalysis.html")
        soup = BeautifulSoup(page.content, 'lxml')
        char = BeautifulSoup(str(soup.find(class_='studyGuideText')), 'lxml')
        ads = char.find_all(class_= 'floatingad')
        strads = []
        text = char.getText()
        for ad in ads:
            strads.append(BeautifulSoup(str(ad), 'lxml').getText())
        for ad in strads:
            text = text.replace(ad, '')
        while '\n' in text:
            text = text.replace('\n', '<br>')
    return text

def themize():
    text = ""
    if shmoopurl:
        page = requests.get(shmoopurl + "themes.html")
        soup = BeautifulSoup(page.content, 'lxml')
        themes = BeautifulSoup(str(soup.find(class_ = 'btn-color-cycle-long')),'lxml')
        links = themes.find_all('a')
        urls = []
        for link in links:
            x = BeautifulSoup(str(link), 'lxml')
            tag = x.a
            urls.append(tag['href'])
        for url in urls:
            page = requests.get(shmoopurl + url)
            soup = BeautifulSoup(page.content, 'lxml')
            descript = BeautifulSoup(str(soup.find(class_ = 'content-learning-guide')), 'lxml')
            title = descript.find('h1')
            par = descript.find_all('p')
            text += "<h1>" + title.getText() + "</h1>"
            i = 0
            while i < len(par) - 4:
                text += par[i].getText()
                i += 1
            while "\n" in text:
                text = text.replace('\n', '<br>')
    elif sparkurl:
        page = requests.get(sparkurl + "themes.html")
        soup = BeautifulSoup(page.content, 'lxml')
        themes = BeautifulSoup(str(soup.find(class_='studyGuideText')), 'lxml')
        ads = themes.find_all(class_= 'floatingad')
        strads = []
        text = themes.getText()
        for ad in ads:
            strads.append(BeautifulSoup(str(ad), 'lxml').getText())
        for ad in strads:
            text = text.replace(ad, '')
        while '\n' in text:
            text = text.replace('\n', '<br>')
    return text

def chapterize():
    text = ""
    if shmoopurl:
        page = requests.get(shmoopurl + 'summary.html')
        soup = BeautifulSoup(page.content, 'lxml')
        chapters = soup.find_all(class_ = 'inner-list')
        urls = []
        for chapter in chapters:
            x = BeautifulSoup(str(chapter), 'lxml')
            tag = x.a
            urls.append(tag['href'])
        for url in urls:
            page = requests.get(shmoopurl + url)
            soup = BeautifulSoup(page.content, 'lxml')
            descript = BeautifulSoup(str(soup.find(class_ = 'content-learning-guide')), 'lxml')
            title = descript.find('h1')
            par = descript.find(class_ = 'PrimaryContent')
            text += "<h1>" + title.getText() + "</h1>" + par.getText()
            while "\n" in text:
                text = text.replace('\n', '<br>')
    elif sparkurl:
        page = requests.get(sparkurl)
        soup = BeautifulSoup(page.content, 'lxml')
        content = soup.find_all(class_ = 'entry odd') + soup.find_all(class_ = 'entry even')
        links = []
        urls = []
        for div in content:
            if "section" in str(div):
                links += div
        for link in links:
            x = BeautifulSoup(str(link), 'lxml')
            tag = x.a
            urls.append(tag['href'])
        sortedurls = []
        for url in urls:
            sortedurls.append(int(url.replace('.rhtml','').replace('section','')))
        sortedurls.sort()
        for num in sortedurls:
            for url in urls:
                if str(num) in url:
                    x = url
                    urls.remove(url)
                    urls.append(x)
        for url in urls:
            text += "<h1>" + url.replace('.rhtml', '').upper() + "</h1> <br>"
            page = requests.get(sparkurl + url)
            soup = BeautifulSoup(page.content, 'lxml')
            chap = BeautifulSoup(str(soup.find(class_='studyGuideText')), 'lxml')
            ads = chap.find_all(class_= 'floatingad')
            strads = []
            text += chap.getText()
            for ad in ads:
                strads.append(BeautifulSoup(str(ad), 'lxml').getText())
            for ad in strads:
                text = text.replace(ad, '')
            while '\n' in text:
                text = text.replace('\n', '<br>')
    return text

HTML_HEADER = """
<!DOCTYPE html>
<html>
<head>
    <title>"""+ book +"""</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet"
    href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link rel="shortcut icon" href="icon.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>
<body>
<a href="http://lisa.stuycs.org/~david.doktorman/tldr.html" class="btn btn-primary btn-lg active" role="button">Back to home</a>
<h1><center> TL;DR of """ + book + """: </center></h1><br><br>
"""

HTML_FOOTER = """
</body>
</html>
"""



html = HTML_HEADER + """<center><div class="container">
  <button type="button" class="btn btn-warning" data-toggle="collapse" data-target="#gensum">General Summary </button>
  <div id="gensum" class="collapse">"""+  summarize().encode('ascii', 'ignore') + """</div></div><br>
  <div class="container">
  <button type="button" class="btn btn-warning" data-toggle="collapse" data-target="#chap">Chapter by Chapter Summary </button>
  <div id="chap" class="collapse">"""+  chapterize().encode('ascii', 'ignore') + """
  </div></div><br>
  <div class="container">
  <button type="button" class="btn btn-warning" data-toggle="collapse" data-target="#theme">Themes </button>
  <div id="theme" class="collapse">"""+  themize().encode('ascii', 'ignore') + """
  </div></div><br><div class="container">
  <button type="button" class="btn btn-warning" data-toggle="collapse" data-target="#char">Character Analysis </button>
  <div id="char" class="collapse">"""+  characterize().encode('ascii', 'ignore') + """
  </div></div><br></center>""" + HTML_FOOTER
print html