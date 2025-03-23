import requests
from bs4 import BeautifulSoup

def get_news_articles(company):
    url = f"https://news.google.com/search?q={company}&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.find_all("article")[:10]:
        # recursive call 
        title = item.get_text(' ') if item.find("h3") else "No Title"
        link = soup.find("a")["href"] if item.find("a") else "#"
        summary = item.find("p").get_text() if item.find("p") else "No Summary"
        Button = item.find("button").text if item.find("button") else "No button"
        articles.append({"Title": title, "Summary": summary, "link": link})

    return {"Company": company, "Articles":articles}

# import requests
# from bs4 import BeautifulSoup

# URL = 'https://news.google.com/search?q=google&hl=en-IN&gl=IN&ceid=IN:en'
# r = requests.get(URL)
# soup = BeautifulSoup(r.text, 'html.parser')

# for item in soup.find_all('article')[:2]:
#     for atags in item.find_all('a'):
#         print(atags.text)
#         link1 = 'https://news.google.com'+atags['href'].lstrip('.')
#         print(link1)