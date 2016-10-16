from SpiderPackage import URLmanager
from SpiderPackage import htmlDownloader
from SpiderPackage import htmlOutput
from SpiderPackage import htmlParser


class SpiderMain(object):
    def __init__(self):
        self.urls = URLmanager.UrlManager()
        self.downloader = htmlDownloader.HtmlDownloader()
        self.parser = htmlParser.HtmlParser()
        self.output = htmlOutput.HtmlOutputer()

    def craw(self, root_url):
        print "I am here1"
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count == 2:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.output.output_html()
        pass


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python/407313.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)



