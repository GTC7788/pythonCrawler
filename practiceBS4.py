from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)
print(soup.p['class'])

for l in soup.find_all('p'):
    print(l.get('class'))


print "regular expression"
linkname = soup.find('a', href = re.compile("ill"))
print linkname .name, linkname['href'],linkname.get_text()

print 'get the passage content'
linknode = soup.find('p',class_ = "title")
print linknode, linknode.get_text()
