import requests


BASE_URL = 'https://www.rescale.com/'
class Crawler(object):
    """Class that crawls a top level url and all subsequent urls listed in the initial document.

    Args:
        object ([type]): [description]
    """


    def __init__(self):
        resp = requests.get(BASE_URL)

        resp.raise_for_status

        text = resp.text

        print(text)


if __name__ == "__main__":
    print('Initial testing')

    crawler = Crawler()
