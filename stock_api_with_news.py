import requests
from twilio.rest import Client

# Twilio_data
SID = "ACfd5bbcb573babf4806e355959e3d856a"
A_TOKEN = "2af760ef0a4d4ae5290a3e5eefe479f0"
# News_data
NEWS_URL = "https://newsapi.org/v2/everything?q=TSLA&from=2022-12-21&sortBy=papularity&sources=bbc-news,the-verge&language=en&apiKey=591b56d28e0345fd929ae1896ae512dd"
# Stock_data
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "TZ4TCC4BPHK7UMFQ"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

Stock_dict = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": "TZ4TCC4BPHK7UMFQ"
}

class Stock_exchange:
    def __init__(self):
        # STOCK RESPONSE
        self.difference_percentage = None
        self.difference = None
        self.yesterday_close = None
        self.day_before_yesterday_close = None
        self.yesterday = None
        self.day_before_yesterday = None
        self.stock_response = requests.get(STOCK_ENDPOINT, params=Stock_dict)
        self.stock_data = self.stock_response.json()["Time Series (Daily)"]
        # NEWS RESPONSE
        self.news_response = requests.get(NEWS_URL)
        self.news_data = self.news_response.json()
        # TWILIO DATA
        self.client = Client(SID, A_TOKEN)
        self.msg_dict = {
            "ARTICLES": []
        }
        self.Difference = 0
        self.r_f = ''

    def news_api(self):
        self.articles = [news for news in self.news_data["articles"][:3]]
        self.formated_articles = [
            f"TSLA {self.difference_percentage}%{self.r_f}\nHEADLINE:{self.articles[item]['title']}\nBREIF:{self.articles[item]['description']}"
            for item in range(len(self.articles))]

    def twilio_api(self):
        for msg in self.formated_articles:
            message = self.client.messages.create(
                from_='whatsapp:+14155238886',
                body=f"{msg}",
                to='whatsapp:+923020111017'
            )
            print(message.status)

    def stock_api(self):
        self.data_list = [self.value for (self.key, self.value) in self.stock_data.items()]
        self.yesterday = self.data_list[0]
        self.day_before_yesterday = self.data_list[1]
        self.yesterday_close = self.yesterday["4. close"]
        self.day_before_yesterday_close = self.day_before_yesterday["4. close"]
        self.difference = float(self.yesterday_close) - float(self.day_before_yesterday_close)
        if self.difference > 0:
            self.r_f = "🔺"
        else:
            self.r_f = "🔻"

        self.difference_percentage = round(self.difference * 100 / float(self.yesterday_close))


# Main
stock = Stock_exchange()
stock.stock_api()
stock.news_api()
stock.twilio_api()
