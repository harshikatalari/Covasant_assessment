import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import os

def download_url(url):
    try:
        response = requests.get(url, timeout=10)
        path = urlparse(url).path
        filename = os.path.basename(path) or "index.html"
        filename = filename.replace("/", "_")  

        with open(filename, "wb") as f:  # we use 'wb' here for binary content
            f.write(response.content)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def get_all_links(base_url):
    try:
        response = requests.get(base_url)    
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            full_url = urljoin(base_url, a_tag['href']) #joining baseurl with hreference
            if full_url.startswith("http"):   #if file ends with http appending link to links list []
                links.append(full_url)
        return links
    except Exception as e:
        print(f"Failed to parse the links from {base_url}: {e}")
        return []

def download_all_links(base_url):
    print(f"Parsing and downloading links from: {base_url}") #here baseurl has many sub urls
    links = get_all_links(base_url)           #links is list of all the links in baseurl
    print(f"Found {len(links)} links.")   #returns length of links found in given base_url

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_url, links)


if __name__ == '__main__':
    base_url = "https://www.tpointtech.com/python-tutorial" #we can use any url here
    download_all_links(base_url)
