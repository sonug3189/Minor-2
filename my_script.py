
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tweets_data = pd.read_csv('Tweets.csv')


# In[4]:


mood_count = tweets_data['airline_sentiment'].value_counts()


# In[5]:


mood_count


# In[6]:


tweets_data['airline'].value_counts()


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


Index = [1,2,3]
plt.bar(Index, mood_count)
plt.xticks(Index, ['neg', 'neutral', 'pos'])
plt.ylabel('Sentiment Count')


# In[9]:


df_airline_united = tweets_data[tweets_data['airline'] == 'United']


# In[11]:


# from wordcloud import WordCloud, STOPWORDS


# In[12]:


# df = tweets_data[tweets_data['airline_sentiment'] == 'negative']


# In[13]:


# df.head()


# In[14]:


# words = ' '.join(df['text'])


# In[15]:


# wordcloud = WordCloud(stopwords = 
#                       STOPWORDS, background_color='black', 
#                       height = 2500, width = 3000).generate(words)


# In[16]:


# plt.imshow(wordcloud)
# plt.axis('off')


# In[17]:


# tweets_data['sentiment'] = tweets_data['airline_sentiment'].apply(

# lambda x: 0 if x =='negative' else 1)


# In[11]:


from nltk.corpus import stopwords


# In[19]:


def tweet_to_words(raw_tweet):

    words = raw_tweet.lower().split()
    stopw = set(stopwords.words("english"))
    
    meaningful_words = [w for w in words if not w in stopw]
    
    return (" ".join(meaningful_words))


# In[20]:


#tweets_data['clean_tweets'] = tweets_data['text'].apply(tweet_to_words)


# In[12]:


data = tweets_data['text']


# In[13]:


target = tweets_data['airline_sentiment']


# In[14]:


from sklearn.cross_validation import train_test_split


# In[15]:


x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)


# In[16]:


xtest=x_test
xtrain = x_train
ytrain = y_train
ytest=y_test


# In[17]:


from sklearn.feature_extraction.text import CountVectorizer


# In[18]:


v = CountVectorizer(analyzer = "word", ngram_range = (1,2))


# In[33]:


xtrain.reset_index(drop = True , inplace = True)


# In[34]:


ytrain.reset_index(drop = True , inplace = True)


# In[37]:


train_features = v.fit_transform(xtrain)


# In[35]:


xtest.reset_index(drop = True , inplace = True)


# In[36]:


ytest.reset_index(drop = True , inplace = True)


# In[40]:

file = open("test_file.txt", "r") 

xtest[3] = str(file.read())


# In[41]:


test_features = v.transform(xtest)


# In[42]:


from sklearn.tree import DecisionTreeClassifier


# In[43]:


clf = DecisionTreeClassifier()
clf.fit(train_features, y_train)
clf.score(test_features, y_test)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(train_features, y_train)
clf.score(test_features, y_test)
temp = clf.predict(test_features[3])
file = open("test_file.txt","w") 
file.write(temp) 

file.close()  