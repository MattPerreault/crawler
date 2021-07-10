import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://www.rescale.com'
class Crawler(object):
    """Class that crawls a top level url and all subsequent urls listed in the initial document.
    """


    def __init__(self, url):
        """Class constructor takes in a valid url as an argument, rescale.com is the default if nothing is passed in.
        Attempts to make get request to url, raises and exception if it fails.
        Returns the contents of the page as 
        Args:
            url (str): Valid url example: https://www.rescale.com/.
        """
        self.url = url
        self.resp = requests.get(self.url)
        self.resp.raise_for_status
        self.html_content = BeautifulSoup(self.resp.content, "html.parser")

    def get_links(self) -> set:
        """Gets all urls from page, puts them into a list

        Returns:
            list: Containing all urls on a page
        """
        links = set()
        for link in self.html_content.find_all('a'):
            href = link.get('href')

            if href is None:
                continue
            elif href.startswith('/'):
                links.add(self.url+href)
            else:
                links.add(href)
        return links

if __name__ == "__main__":
    print('Starting crawl..')
    crawler = Crawler(BASE_URL)

    print('Fetching links..')
    links = crawler.get_links()

    for link in links:
        print(link)
