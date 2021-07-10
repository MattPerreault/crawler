import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://www.rescale.com/'
class Crawler(object):
    """Class that crawls a top level url and all subsequent urls listed in the initial document.

    Args:
        object ([type]): [description]
    """


    def __init__(self):
        resp = requests.get(BASE_URL)

        resp.raise_for_status

        html_content = BeautifulSoup(resp.content, "html.parser")

        print(html_content.prettify)


if __name__ == "__main__":
    print('Initial testing...')

    crawler = Crawler()
