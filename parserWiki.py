import re
import urlparse
from bs4 import BeautifulSoup

# This is a basic parser program, by using BeautifulSoup, it can find all URLs in the form: wikipedia.org/wiki/***
# Those URLs are added to the URLmanager for further crawl.
#
# Wikipedia html content example:


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set() # Set avoid duplicate URLs
        links = soup.find_all('a', href = re.compile(r"/wiki/(\w)"))  # The regular expression here still need improve.
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['rul'] = page_url

        # <h1 id="firstHeading" class="firstHeading" lang="en">Recursive neural network</h1>
        # title_node = soup.find('h1', class_= "firstHeading"
        title_node = soup.find('div', class_= "mw-body").find("h1", class_ = "firstHeading")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        "mw-content-ltr"
        summary_node = soup.find('div', class_ = "mw-body-content").find('div', class_ = "mw-content-ltr").find("p")
        res_data['summary'] = summary_node.get_text()
        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

