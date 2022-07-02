import requests
import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
params={"function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
        "apikey":"UWXWH9DOX2VL08KS"}
listarr=[]
paramsn={"q":"tesla",
        "from":datetime.date.today(),
         "sortBy":"publishedAt",
         "apiKey":"7b5d1ba5227a487aa29f79643eb6a233"}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response=requests.get(url = 'https://www.alphavantage.co/query',params=params)
response.raise_for_status()
data=response.json()
for day in data["Time Series (Daily)"]:
        listarr.append(float(data["Time Series (Daily)"][day]["4. close"]))
        if len(listarr)==2:
                break

growth=listarr[0]-listarr[1]
percent=round((((listarr[0]+growth)-listarr[0])/listarr[0])*100,2)
if percent < -1 or percent > 1:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    responsen=requests.get(url="https://newsapi.org/v2/everything",params=paramsn)
    responsen.raise_for_status()
    news=responsen.json()
    title=news["articles"][0]["title"]
    desc=news["articles"][0]["description"]
    if percent>0:
        print(f" {STOCK} : 🔺 {percent}% \n Headline : {title}\n Brief:{desc}")
    else:
        print(f" {STOCK} : 🔻{percent}% \n Headline : {title}\n Brief:{desc}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

