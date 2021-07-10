import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://www.rescale.com/'
class Crawler(object):
    """Class that crawls a top level url and all subsequent urls listed in the initial document.
    """


    def __init__(self, url=BASE_URL):
        """Class constructor takes in a valid url as an argument, rescale.com is the default if nothing is passed in.
        Attempts to make get request to url, raises and exception if it fails.
        Returns the contents of the page as 
        Args:
            url (str): Valid url example: https://www.rescale.com/. Defaults to BASE_URL.
        """
        self.resp = requests.get(BASE_URL)
        self.resp.raise_for_status
        self.html_content = BeautifulSoup(self.resp.content, "html.parser")

    def get_links(self) -> list:
        """Gets all urls from page, puts them into a list

        Returns:
            list: Containing all urls on a page
        """
        links = []
        for link in self.html_content.find_all('a'):
            href = link.get('href')
            if href is None:
                continue
            elif "https" in href:
                links.append(href)

if __name__ == "__main__":
    print('Starting crawl..')

    crawler = Crawler()
    links = crawler.get_links()
