import requests
from bs4 import BeautifulSoup
import html.parser
from urllib.parse import urljoin
from textwrap import wrap

def get_all_urls(url):
    """Gets all URLs from a given domain."""

    urls = []
    visited = []
    x = 0

    def crawl(url):
        
        print(f"#{len(urls)}:  {url}")
        if url in visited or len(urls) > 50:
            return
        visited.append(url)


        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/'):
                    href = urljoin(url, href)
                if href.startswith(url):
                    urls.append(href)
                    crawl(href)

        except requests.exceptions.RequestException as e:
            print(f"Error crawling {url}: {e}")

    crawl(url)
    return urls

if __name__ == '__main__':
    domain = "https://www.example.com/"
    all_urls = get_all_urls(domain)
    for url in all_urls:
        print(url)

def web_scrape_all(domain:str):
    site = get_all_urls(domain)
    soup = []
    z = 0
    for i in site:
        z += 1
        print(f"{z} {i}")
        r = requests.get(i)
        x = BeautifulSoup(r.content, 'html.parser').get_text()
        soup.append(x)
    f = open('yahoo_data.txt', 'w')
    f.write(f"{soup}")
    f.close
    return soup

    

scraped_data = web_scrape_all("https://finance.yahoo.com/")



