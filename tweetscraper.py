import pandas as pd
import numpy as np
import csv
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime as dt
import time


from datetime import datetime, timedelta
now = datetime.now()
now = now.strftime('%Y-%m-%d')
yesterday = datetime.now() - timedelta(days = 1)
yesterday = yesterday.strftime('%Y-%m-%d')
start_day=datetime.now() - timedelta(days = 200)
end_day=datetime.now() - timedelta(days = 150)

start_day=start_day.strftime('%Y-%m-%d')
end_day=end_day.strftime('%Y-%m-%d')
keyword = input('Enter a topic or keyword, please:')


maxTweets = 20000


a=[]
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:fa since:' +  start_day + ' until:' +end_day+'-filter:links -filter:replies' ).get_items()):
        if i > maxTweets :
            break
        a=a+[tweet.content]
with open(keyword +'-sentiment-' + now + '.txt', "w") as f:
    for i in range(len(a)):
        f.write(str(a[i])+'\n'+'\n'+'\n'+'\n'+'\n')
           
