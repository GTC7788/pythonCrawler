import urllib2

# Use urllib2.urlopen to download the content of a html page.

class HtmlDownloader(object):



    def download(self, url):

        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
