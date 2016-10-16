import urllib2
import cookielib


url = "http://www.baidu.com"



print 'The 1st Method'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())


print "The 2nd Method"
request = urllib2.Request(url)
request.add_header("user-agent","Mozillar/5.0")
response2 = urllib2.urlopen(url)
print response2.getcode()
print len(response2.read())


print "The 3rd Method"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()
