import requests
from stock_api import get_stock_api
from news_api import get_new_api
import json
from datetime import date, timedelta, datetime
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":get_stock_api()
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

TSLA_data = response.json()


try: 
    time_line = TSLA_data["Time Series (Daily)"]
except KeyError:
    with open('./TSLA_INFO.json','r') as TSLA_JSON_FILE:
        TSLA_data = json.load(TSLA_JSON_FILE)
        time_line = TSLA_data["Time Series (Daily)"]

time_line_list = [item for item in time_line.items()]

print(time_line_list[0][0])
print(time_line_list[0][1]['4. close'])

last_update_close = time_line_list[0][1]['4. close']
print(last_update_close)

#TODO 2. - Get the day before yesterday's closing stock price
before_last_update_close = time_line_list[1][1]['4. close']
print(before_last_update_close)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(float(last_update_close) - float(before_last_update_close))
print('positive_difference : ', positive_difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (positive_difference/ float(last_update_close))*100
print(f'diff_percent: {diff_percent}')
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

if diff_percent > 1:
    print("Get News")
    news_params={
        "apiKey": get_new_api(),
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params =news_params)
    articles = news_response.json()["articles"]
    three_articles  = articles[:3]





    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

#TODO 9. - Send each article as a separate message via Twilio. 
    
    AccountSID_Live="" 
    Auth_Token_Live=""  

    client = Client(AccountSID_Live, Auth_Token_Live)

    for article in formatted_articles:
        message = client.messages.create(
          from_='+14253584238',
          body=article,
          to='+525516918487'
        )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

