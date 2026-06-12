import requests
from config import NEWS_API_KEY


def get_news(category):

    url = (
        "https://newsapi.org/v2/top-headlines"
        f"?category={category}"
        "&country=de"
        f"&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    articles = data.get("articles", [])[:5]

    news_text = ""

    for article in articles:
        title = article.get("title", "")
        news_text += f"• {title}\n"

    return news_text
