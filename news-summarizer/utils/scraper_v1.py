import requests
from bs4 import BeautifulSoup

def get_articles_list(company_name:str) -> dict:
    URL = f'https://www.bbc.com/search?q={company_name}'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    i = 0 
    titles=[]
    urls=[]

    # for item in soup.find_all('article')[:5]:
    #     i +=1
    #     for a_tags in item.find_all('a'):
    #         if a_tags.text!='':
    #             titles[i] = a_tags.text
    #             url[i]='https://news.google.com'+a_tags['href'].lstrip('.')
    # return titles,url
    for title in soup.find_all('h2')[:10]:
        titles.append(title)
    for url in soup.find_all('a',class_='sc-2e6baa30-0 gILusN')[6:15]:
        urls.append('https://www.bbc.com'+url['href'])
        print(('https://www.bbc.com'+url['href']))
    return titles,urls


import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """Extract all text from a given webpage URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)  # Extract text

        return text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_text_from_article(urls):
    """Extract text from multiple URLs."""
    extracted_texts = {}
    
    for url in urls:
        print(f"Extracting urls")
        text = extract_text_from_url(url)
        if text:
            # print(text)
            extracted_texts[url] = text[:1000]  # Store first 1000 chars for preview
    
    return extracted_texts

# Example Usage:


def main(company_name):
    titles, urls = get_articles_list(company_name=company_name)
    results = extract_text_from_article(urls)
    
    # for url, text in results.items():
        # print(f"\nText from :\n{text[:500]}...")  # Print first 500 characters

    return list(results.values())
