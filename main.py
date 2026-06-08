import schedule
import time

from news import get_news
from ai_summary import summarize
from whatsapp import send_whatsapp


def morning_news():

    print("Fetching news...")

    sports = get_news("sports")

    politics = get_news("general")

    ai_news = get_news("technology")

    combined_news = f"""
SPORTS

{sports}

POLITICS

{politics}

AI

{ai_news}
"""

    print("Generating summary...")

    summary = summarize(combined_news)

    print("Sending WhatsApp message...")

    send_whatsapp(summary)

    print("Done")


# Run once immediately
morning_news()

# Schedule every day at 07:00
schedule.every().day.at("07:00").do(
    morning_news
)

while True:
    schedule.run_pending()
    time.sleep(60)