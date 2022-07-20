#Title: Exploratory Data Analysis for SurgeAI Dataset
#Author: Ebuwa Evbuoma-Fike
#Last Edited: 07/14/2022

#Import packages
import re
import string
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import graph_objs as go
import plotly_express as px
import plotly.figure_factory as ff
from collections import Counter

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


import nltk
from nltk.corpus import stopwords

from tqdm import tqdm
import os
import nltk
import spacy
import random
from spacy.util import compounding
from spacy.util import minibatch

import string
import emoji
import re, string
from nltk import word_tokenize
from nltk.corpus import stopwords

ps = nltk.PorterStemmer()
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))

import warnings
warnings.filterwarnings("ignore")

#Read in SurgeAI csv as traindata

traindata = pandas.read_csv("/Volumes/GoogleDrive/My Drive/Time at Brown School/Summer 2022/Correlation One Data Science for All/Resources/project31/data/train.csv")

print(traindata)

traindata.head()

traindata.columns


#Select analytical columns into new dataframe called df
df = traindata[[ 'is_reviewed','text', 'username', 'bio', 'Categorize the tweet']]

df = df.rename(columns = {"Categorize the tweet": "sentiments"})

#Read the analytical dataframe

print(df.shape)
#(1025, 6)

df.describe()
#       Num_word_text
#count    1025.000000
#mean       19.107317
#std         4.412805
#min         1.000000

df.info()
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 1025 entries, 0 to 1024
#Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype
#---  ------         --------------  -----
# 0   is_reviewed    1025 non-null   bool
# 1   text           1025 non-null   object
# 2   username       1025 non-null   object
# 3   bio            866 non-null    object
# 4   sentiments     1025 non-null   object
# 5   Num_word_text  1025 non-null   int64
#dtypes: bool(1), int64(1), object(4)
#memory usage: 41.2+ KB

#Examine the distribution of tweets in the dataframe using color codes
temp = df.groupby('sentiments').count()['text'].reset_index().sort_values(by='text',ascending=False)

temp.style.background_gradient(cmap='Purples')

#Examine the distribution of word counts (number of words per tweet)
df['Num_word_text'] = df['text'].apply(lambda x:len(str(x).split()))

df[df.sentiments == 'Pro-life']['Num_word_text']

#Create two new series grouped by sentiment, pro-life and pro-choice

data1 = df[df.sentiments == 'Pro-life']['Num_word_text']
data2 = df[df.sentiments == 'Pro-choice']['Num_word_text']

#Plot the distribution of number of words per tweet by sentiment
plt.figure(figsize=(8,6))
plt.hist(data1, bins=10, alpha=0.5, label="pro-choice") #Histogram for Pro-choice Sentiment
plt.hist(data2, bins=10, alpha=0.5, label="pro-life")   #Histogram for Pro-life Sentiment
plt.xlabel("Number of words per Tweet", size=14)
plt.ylabel("Count", size=14)
plt.title("Distribution of Number of Words per Tweet by Sentiment ")
plt.legend(loc='upper right')
#Longer tweets tend to be pro-choice, distribution is right skewed

#Plot a Funnel-Chart for better visualization
fig = px.funnel(df, x= "Num_word_text", y= "sentiments")
fig.show()

#link: http://127.0.0.1:64617/

