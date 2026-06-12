import schedule
import time
import pytz

from datetime import datetime

from news import get_news
from ai_summary import summarize
from whatsapp import send_whatsapp

GERMANY_TZ = pytz.timezone(
    "Europe/Berlin"
)

last_sent_date = None

def morning_news():

    print(
        "Fetching latest news..."
    )

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

    print(
        "Generating AI summary..."
    )

    summary = summarize(
        combined_news
    )

    print(
        "Sending WhatsApp message..."
    )

    send_whatsapp(summary)

    print(
        "News sent successfully."
    )

def germany_scheduler():

    global last_sent_date

    germany_now = datetime.now(
        GERMANY_TZ
    )

    current_date = germany_now.date()

    current_time = germany_now.strftime(
        "%H:%M"
    )

    if (
        current_time == "08:30"
        and last_sent_date != current_date
    ):

        morning_news()

        last_sent_date = current_date

schedule.every(1).minutes.do(
    germany_scheduler
)

print(
    
"Scheduler started."
)
schedule.every().day.at("07:00").do(
    morning_news
)

if __name__ == "__main__":
    morning_news()
if __name__ == "__main__":
    print("Bot started")

    while True:
        schedule.run_pending()
        time.sleep(30)
