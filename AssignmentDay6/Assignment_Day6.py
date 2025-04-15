import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os


os.makedirs("downloads", exist_ok=True) # Creates a 'downloads' folder if not exists
async def download_page(session, url):
    try:
        async with session.get(url,timeout=10) as response:  # Sends an HTTP GET request with timeout
            content= await response.read()
            filename = urlparse(url).path.replace('/' , '_') or 'index.html' 
            filepath=os.path.join("downloads",filename) #making full file path to save content
            with open(filepath, 'wb') as f:  # Opens the file in binary write mode
                f.write(content)
                print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}:{e}")

async def get_all_links(session, base_url):
    try:
       async with session.get(base_url, timeout=10) as response:   # Sends HTTP GET request
           html=await response.text()              # Reads response content as text
           soup=BeautifulSoup(html, 'html.parser')
           links=[]
           for a in soup.find_all('a', href=True):
               full_url=urljoin(base_url, a['href'])
               if full_url.startswith("http"):
                  links.append(full_url)     #links is list of all the links in baseurl
           return links                         #returns length of links found in given base_url
    except Exception as e:
        print(f"Failed to parse the links from {base_url}: {e}")
        return []

async def main(base_url):
    async with aiohttp.ClientSession() as session:         # Creating a session for making HTTP requests
        print(f"fetching and parsing main page : {base_url}")
        links= await get_all_links(session, base_url)
        print(f"Found {len(links)} links")        # Gets all links from baseurl
        tasks= [download_page(session, url) for url in links]     #Preparing download tasks for all links
        await asyncio.gather(*tasks)   #Runs all download tasks concurrently


if __name__ == '__main__':
    test_url = "https://www.tpointtech.com/python-tutorial" #we can use any url here
    asyncio.run(main(test_url))
