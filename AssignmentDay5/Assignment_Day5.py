import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import os

def download_url(url):
    try:
        response = requests.get(url, timeout=10)                # Sending an HTTP GET request with a 10-second timeout
        path = urlparse(url).path                               # Extracting the path part from the URL
        filename = os.path.basename(path) or "index.html"       # Gets the filename from the path or will use "index.html" if its empty
        filename = filename.replace("/", "_")  

        with open(filename, "wb") as f:  # Opens the file in binary write mode
            f.write(response.content)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def get_all_links(base_url):
    try:
        response = requests.get(base_url)                       # Sends a GET request to the base URL
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            full_url = urljoin(base_url, a_tag['href'])         #making full file path to save content
            if full_url.startswith("http"):                     #if file ends with http appending link to links list []
                links.append(full_url)
        return links
    except Exception as e:
        print(f"Failed to parse the links from {base_url}: {e}")
        return []

def download_all_links(base_url):
    print(f"Parsing and downloading links from: {base_url}") 
    links = get_all_links(base_url)                             #links is list of all the links in baseurl
    print(f"Found {len(links)} links.")                         #returns length of links found in given base_url

    with ThreadPoolExecutor(max_workers=5) as executor:         # Creates a thread pool with 5 worker threads
        executor.map(download_url, links)                       # Distributes the downloading task across threads


if __name__ == '__main__':
    base_url = "https://www.tpointtech.com/python-tutorial"      #we can use any url here
    download_all_links(base_url)

    
     
