import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = []
        for item in soup.find_all('h2'):
            headlines.append(item.get_text())

        return headlines

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

news_url = "https://timesnownews.com"
headlines = get_headlines(news_url)

if headlines:
    print("Today's Headlines:")
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}, {headline}")
else:
    print("No headlines found")