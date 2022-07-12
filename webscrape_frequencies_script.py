#Title: Script to Scrape Tweets & Count Hashtag Frequencies
# Adapted from: AI Spectrum and v1 shared by Taiwo Owoseni
# Author: Ebuwa Evbuoma-Fike
# Last Edited: 07-10-2022

"""Downloads xls data from the web to a local filepath as csv file.
"""
#Import snscrape, pandas, datetime and counter packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime as dt
from collections import Counter
import matplotlib.pyplot as plt

#Create lists called tweets and hashtag_list
tweets = []
hashtag_list = []

#Set limit on webscrape
limit = 50000

#Create date class
today_date = dt.date.today().strftime("%Y-%m-%d")

#Populate query_list
query_list = [
    (f"(TheCircle (#TheCircle) lang:en  since:2022-07-01 until:{today_date})"),
    (f"(theCircle (#TheCircleNetflix) lang:en  since:2022-07-01 until:{today_date})"),
    (f"(TheCircle (#TheCircleNetflix) lang:en  since:2022-07-01 until:{today_date})"),
    (f"(thecircle (#TheCircle) lang:en  since:2022-07-01 until:{today_date})"),
    (f"(the circle (#TheCircle) lang:en  since:2022-07-01 until:{today_date})"),
    (f"(the circle (#TheCircleNetflix) lang:en  since:2022-07-01 until:{today_date})"),
    (f"(the circle (#TheCircle4) lang:en  since:2022-07-01 until:{today_date})"),
]

#Create function extract_hash_tags
def extract_hash_tags(s):
    return list(set(part[1:] for part in s.split() if part.startswith('#')))

#Execute loops
for query in query_list:
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) > limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content, extract_hash_tags(tweet.content)])

for twt in tweets:
    hashtag_list.extend(twt[-1])
df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet", "hashtags"])

#Save output to csv
df.to_csv("0710TwitterMine.csv")

#Print the frequency of each hashtag in hashtag_list
print(Counter(hashtag_list))

#Sort output decreasing
hashtag_list.sort(reverse=True)
