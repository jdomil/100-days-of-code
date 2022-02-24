import os
import requests
from twilio.rest import Client
import math

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}

ACCOUNT_SID = "AC188204ec1465c13b35a213a92cbc73a2"


def get_news() -> list:
    """Returns 3 last articles data for COMPANY_NAME"""
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    titles = [article for article in articles]
    return titles[:3]


def send_message(articles: list, variation: float):
    """Sends a separate message with the percentage change and each article's title and description in articles list"""
    if variation > 0:
        icon = "🔺"
    else:
        icon = "🔻"

    variation_display = abs(math.floor(variation))
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in articles:
        headline = article["title"]
        description = article["description"]
        # print(f"{STOCK}: {icon}{variation_display}%\n"
        #       f"Headline: {headline}\n"
        #       f"Brief: {description}")
        message = client.messages.create(
            body=f"{STOCK}: {icon}{variation_display}%\n"
                 f"Headline: {headline}\n"
                 f"Brief: {description}",
            from_="+19032963763",
            to=os.environ.get("MY_PHONE")
        )

        print(message.status)


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then call get_news().
stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()

daily_stock_data = (stock_data["Time Series (Daily)"])
data_list = [value for (key, value) in daily_stock_data.items()]
yesterday_close_price = float(data_list[0]["4. close"])
day_before_yesterday_close_price = float(data_list[1]["4. close"])
percentage_price_variation = (yesterday_close_price - day_before_yesterday_close_price) \
                             / day_before_yesterday_close_price * 100

# print(day_before_yesterday_close_price)
# print(yesterday_close_price)
# print(percentage_price_variation)

if abs(percentage_price_variation) >= 5:
    articles_list = get_news()
    send_message(articles_list, percentage_price_variation)


# SMS Format
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

