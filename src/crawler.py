import argparse
import requests

from bs4 import BeautifulSoup

BASE_URL = 'https://www.rescale.com'

# Set of links, use a set to deal with duplicate links.
links = set()

# Keeps track of count of urls visited
urls_count = 0

def get_links(url:str) -> set:
    """Gets all urls from a page puts them into a set

    Args:
        url (str): The url to crawl
    Returns:
        set: Containing all urls on a page
    """
    
    urls = set()

    html_content = get_content(url)

    for link in html_content.find_all('a'):
        href = link.get('href')

        # Check for empty tags
        if href is None or href == "":
            continue
        elif href.startswith('/'):
            site = url+href

        if not is_active(site):
            # check for inactive/broken urls
            continue

        if site in links:
            # check for urls already crawled
            continue
        print(site)
        links.add(site)
        urls.add(site)
    return urls


def is_active(url:str) -> bool:
    """Checks if the url we are parsing is active link.

    Args:
        url (str): [description]

    Returns:
        bool: True if get a 200 response else 
    """
    resp = requests.get(url)

    return True if resp.status_code == 200 else False

def get_content(url:str) -> BeautifulSoup:
    """Attempts to make get request to url, raises HTTPError if it fails.
    Returns the contents of the page.

    Args:
        url (str): Valid url example: https://www.rescale.com. 

    Returns:
        BeautifulSoup: The contents of the html page to parse.
    """
    resp = requests.get(url)
    resp.raise_for_status
    return BeautifulSoup(resp.content, "html.parser")

def crawler(url:str, max_depth=5):
    """Function that crawls the given url and all urls listed on that page
    up to 5 levels deep.

    Args:
        url (str): Valid url to crawl.
        max_depth (int, optional): Number of urls to crawl. Defaults to 5.
    """
    # Set the count to a global for tracking.
    global urls_count 
    urls_count +=  1

    links = get_links(url)

    for link in links:
        if urls_count > max_depth:
            break
        crawler(link, max_depth=max_depth)


def get_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url',
                        dest='url',
                        help='url to crawl',
                        required=True)

    return parser.parse_args()

if __name__ == "__main__":
    args = get_cmd_line_args()
    
    crawler(args.url)

    print(f"Total urls visited: {urls_count}.")
    print(f"Total rescale site urls: {len(links)}")
