from GoogleNews import GoogleNews
import pandas as pd
from gnewsclient import gnewsclient
import pymongo
import random
import wikipedia
import tweepy
import datetime
from pymongo import MongoClient
from datetime import date
from pytrends.request import TrendReq
import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import nltk
import pycountry
import sys

#This class contains the code which interacts with API's such as Twitter, Google , Youtube and Process Them according to 
#the input


#Get Keyword passed from React to Node
userKeywordFromNode = sys.argv[1]
userCategoryFromNode = sys.argv[2]

# keyword to Search + Category
keywordToSearch = userKeywordFromNode

#if keyword contains a country name first Character is uppercase
for country in pycountry.countries:
    keywordToSearch = keywordToSearch.title()
    if country.name in keywordToSearch:
        keywordToSearch = keywordToSearch.title()
        break
    else:
        keywordToSearch = keywordToSearch.lower()

user_keyword_list = [keywordToSearch]
user_category = userCategoryFromNode

# connect to Mongo DB Server
client = MongoClient("mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/test?retryWrites=true&w=majority") #atlas
    
#local server
# client =MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
db = client.test  # test connection if connected

# establishing connection with google trends

try:
    pytrend = TrendReq()
except:
    pytrend = TrendReq()

# code to remove space
from datetime import datetime

dateTimeObj = datetime.now()
clientdatabaseName = keywordToSearch.replace(" ", "")

#if Database was already created on same day python script will not run
dbnames = client.list_database_names()
if clientdatabaseName in dbnames:
    #     client.drop_database(clientdatabaseName)
    mydb = client[clientdatabaseName]
    mycol = mydb["DateCreated"]

    databaseDateCreated = mycol.find_one()
    del databaseDateCreated['_id']
    date_created = databaseDateCreated.get('date created')
    todaysDate = dateTimeObj.strftime("%Y-%m-%d")  # todays date
    if (date_created == todaysDate):
        print("Already Searched")
        sys.exit()
    else:
        print('Not Created Today')

elif clientdatabaseName.lower() in dbnames:
    client.drop_database(clientdatabaseName.lower())


#Similar Tweets Collection
db = client[clientdatabaseName]
db.similartweets.drop()  # delete collection to have fresh collection
similartweetsCollection = db['similartweets']  # new collection for Similar Tweets according to Category

db.keywordandcategorys.drop()  # delete collection to have fresh collection
keywordAndCategoryCollection = db['keywordandcategorys']  # new collection for Keyword and Category
keyowrdAndCategoryDict = {'keyword': keywordToSearch,'Category':user_category}  # creating dict for created date
keywordAndCategoryCollection.insert_one(keyowrdAndCategoryDict)


# Categories and their twitter accounts
sport = ['BBCSport']
business = ['Forbes', 'WSJ', ]
entertainment = ['TwitterMovies', 'hypem']
space = ['SpaceX', 'space', 'NASA']
politics = ['politics']
tech = ['TheNextWeb', 'recode', 'TechCrunch']
health = ['MedlinePlus', 'goodhealth', 'World_Wildlife']

category_account = ''

from datetime import datetime

dateTimeObj = datetime.now()
db = client[clientdatabaseName]  # open database if not available will be created
db.DateCreated.drop()  # delete collection to have fresh collection
DateCreatedCollection = db['DateCreated']  # new collection for Date Created according to Category
todaysDate = dateTimeObj.strftime("%Y-%m-%d")  # todays date

mydict = {'date created': todaysDate}  # creating dict for created date
DateCreatedCollection.insert_one(mydict)

# code to randomly select twitter account according to user category
if user_category == "sport":
    category_account = random.choice(sport)
elif user_category == "business":
    category_account = random.choice(business)
elif user_category == "entertainment":
    category_account = random.choice(entertainment)
elif user_category == "space":
    category_account = random.choice(space)
elif user_category == "tech":
    category_account = random.choice(tech)
elif user_category == "politics":
    category_account = random.choice(politics)
elif user_category == "health":
    category_account = random.choice(health)
else:
    category_account = 'cnnbrk '

# Authentication to twitter
auth = tweepy.OAuthHandler("OVTdS84lJEILeeldhGCUZYNqg", "6QRG9zAdezggILyzPcKH2wzpSHqmpsKSlNXTTPMADrGVQ6lKLr")
auth.set_access_token("405223959-hQfJbDlma2vxkF1YKVvOjFDhJPTIdLnxoNkmiipk",
                      "d18NNIPXQ3yixNB6j0bgaJ6ib6aAz8oHcP0TfmmABfbzn")

api = tweepy.API(auth)

# test authentication
userID = category_account

try:
    # access api get tweets accoring to channel
    tweets = api.user_timeline(category_account, count=5)

    unfilteredList = []  # add all tweets to list
    for each_json_tweet in tweets:
        unfilteredList.append(each_json_tweet._json)
    filteredList = []  # create empty filtered list
    all_data = unfilteredList

    # iterating through the tweets and filtering only the required columns
    for word in all_data:
        tweet_id = word['id']
        text = word['text']
        favorite_count = word['favorite_count']
        retweet_count = word['retweet_count']
        created_at = word['created_at']
        filteredList.append({'text': str(text),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'created_at': created_at,
                             })

    # code to add dictionary to database (MongoDB) collection
    similartweetsCollection.insert_many(filteredList)
except:
    print("NO TWEETS")

try:
    db.similarsearches.drop()  # delete collection to have fresh collection
    SimilarSearchesCollection = db['similarsearches']  # new collection for Similar Tweets according to Category

    keywords = pytrend.suggestions(keyword=keywordToSearch)
    df = pd.DataFrame(keywords)  # adding suggestions to dataframe

    # converting dataframe to dictionary
    data = df
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    SimilarSearchesCollection.insert_many(data_dict)
except:
    print("Cant print similar Searches")

db.searchedcountrys.drop()  # droping collection from db
searchedCountryCollection = db['searchedcountrys']  # creating collection

try:
    # using pytrends to find interest by region
    pytrend.build_payload(user_keyword_list)
    interest_by_region_df = pytrend.interest_by_region(inc_low_vol=False)
    interest_by_region_df = interest_by_region_df.sort_values(by=keywordToSearch, ascending=False)[keywordToSearch]
    geointerest = interest_by_region_df.head(10)
    # convert to Pandas DataFrame
    df = pd.DataFrame(geointerest)
    highest_searched_country = df[keywordToSearch].idxmax()  # country with highest searches

    # converting datframe to dictionary
    data = df
    data = data.rename(columns={keywordToSearch: 'name'})
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    searchedCountryCollection.insert_many(data_dict)  # insert to Database
    df = pd.DataFrame(data_dict)
    countryNames = df['geoName'].tolist()
    values = df['name'].tolist()

#     import numpy as np
#     import matplotlib as mpl
#     import matplotlib.pyplot as plt
#     fig= plt.figure(figsize=(9,6))
#     fig=plt.rcParams['axes.facecolor'] = '#3A3E46'

#     COLOR = 'white'
#     mpl.rcParams['text.color'] = COLOR
#     mpl.rcParams['axes.labelcolor'] = COLOR
#     mpl.rcParams['xtick.color'] = COLOR
#     mpl.rcParams['ytick.color'] = COLOR

#     objects = countryNames
#     y_pos = np.arange(len(objects))
#     performance = values

#     plt.bar(y_pos, performance, align='center', alpha=0.5, color=('#A3A1FB'))
#     plt.xticks(y_pos, objects,rotation=90)
#     plt.ylabel('Search Percentage')
#     plt.title('Total Searches By Country')
#     plt.show
#     plt.savefig('./client/src/components/result-component/searchedcountry.png',transparent=True)
#     plt.savefig('searchedcountry.png',transparent=True)


except:
    if keywordToSearch == keywordToSearch.title():
        keywordToSearch = keywordToSearch.lower()
    else:
        keywordToSearch = keywordToSearch.title()
        # using pytrends to find interest by region
        pytrend.build_payload(user_keyword_list)
        interest_by_region_df = pytrend.interest_by_region(inc_low_vol=False)
        interest_by_region_df = interest_by_region_df.sort_values(by=keywordToSearch, ascending=False)[keywordToSearch]
        geointerest = interest_by_region_df.head(10)
        # convert to Pandas DataFrame
        df = pd.DataFrame(geointerest)
        highest_searched_country = df[keywordToSearch].idxmax()  # country with highest searches

        # converting datframe to dictionary
        data = df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")
        searchedCountryCollection.insert_many(data_dict)  # insert to Database

mydict = {'hishest_Searched_Country': highest_searched_country}  # creating dict for highest searched country


db.mostsearchedcountrys.drop()  # drop collection from db
MostsearchedCountryCollection = db['mostsearchedcountrys']  # create collection
MostsearchedCountryCollection.insert_one(mydict)  # add to collection

db.searcheddates.drop()
searchedDatesCollection = db['searcheddates']
# get the timeframe from current date to previous year
# numdays = 7
# numweeks = 52
# numyears = 1
# total_time_range = numdays * numweeks * numyears
# end_date = date.today()
# today_date = date.today()
# end_date = today_date
# begin_date = end_date - datetime.timedelta(days=total_time_range - 7)
# user_timeframe = begin_date.strftime('%Y-%m-%d') + ' ' + end_date.strftime('%Y-%m-%d')

dateTimeObj = datetime.now()

import datetime
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
lastmonthdate=(lastMonth.strftime("%Y-%m-%d"))

from datetime import date
from datetime import datetime

timestampStr = dateTimeObj.strftime("%Y-%m-%d")    #todays date
mostSearchedToToday=lastmonthdate + " " +timestampStr   #creating timerange from most searched

# use pytrend and pass paraments as required
pytrend.build_payload(kw_list=user_keyword_list, cat=0, timeframe='all', geo='')
interest_over_time = pytrend.interest_over_time()  # get interest over time

df = pd.DataFrame(interest_over_time)  # add to dataframe
dataframeInterestOverTime = df.drop(['isPartial'], axis=1)
most_Searched_Date = dataframeInterestOverTime[keywordToSearch].idxmax()  # country with highest searches

# convert dataframe to dictionary and add to Database
data = dataframeInterestOverTime
data.reset_index(inplace=True)
data_dict = data.to_dict("records")
df = pd.DataFrame(data_dict)
# searchedDatesCollection.insert_many(data_dict)
df = df.rename(columns={keywordToSearch: 'name'})

dates = df['date'].tolist()
values = df['name'].tolist()
datesupdated=[]
x=countryNames[0]
line = str(x)
for x in dates:
    line = str(x)
    time_object = datetime.strptime(line, '%Y-%m-%d %H:%M:%S').date()
    d = time_object.strftime("%m/%d")
    datesupdated.append(d)

# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# fig= plt.figure(figsize=(19,6))
# fig=plt.rcParams['axes.facecolor'] = '#3A3E46'

# COLOR = 'white'
# mpl.rcParams['text.color'] = COLOR
# mpl.rcParams['axes.labelcolor'] = COLOR
# mpl.rcParams['xtick.color'] = COLOR
# mpl.rcParams['ytick.color'] = COLOR

# objects = datesupdated
# y_pos = np.arange(len(objects))
# performance = values

# plt.plot(y_pos, performance, color=('#A3A1FB'))
# plt.xticks(y_pos, objects, rotation=90)
# plt.ylabel('Search Percentage')
# plt.title('Searches from 2004 to Present')
# plt.savefig('./client/src/components/result-component/searcheddates.png',transparent=True)
# plt.savefig('searcheddates.png',transparent=True)



# plt.show()


db = client[clientdatabaseName]  # open database if not available will be created
db.topsearches.drop()  # delete collection to have fresh collection
topSearchescollection = db['topsearches']  # new collection for top searches

db.risingsearches.drop()  # delete collection to have fresh collection
risingSearchescollection = db['risingsearches']  # new collection for Rising Searches

# find related queries for keyword
try:
    try:
        related_queries_dict = pytrend.related_queries()
        topValues = related_queries_dict[keywordToSearch]['top']
        risingValues = related_queries_dict[keywordToSearch]['rising']
        topValues = topValues.head(5)  # get only 5 values
        risingValues = risingValues.head(5)  # get only 5 values
        # convert to DataFrame and then to Dictionary and insert to Database
        topValuesDataFrame = pd.DataFrame(topValues)
        risingValuesDataFrame = pd.DataFrame(risingValues)
        data = topValuesDataFrame
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")
        topSearchescollection.insert_many(data_dict)
        data1 = risingValuesDataFrame
        data1.reset_index(inplace=True)
        data_dict = data1.to_dict("records")
        risingSearchescollection.insert_many(data_dict)
    except:
        related_queries_dict = pytrend.related_queries()
        topValues = related_queries_dict[keywordToSearch]['top']
        risingValues = related_queries_dict[keywordToSearch]['rising']
        topValues = topValues.head(5)  # get only 5 values
        risingValues = risingValues.head(5)  # get only 5 values
        # convert to DataFrame and then to Dictionary and insert to Database
        topValuesDataFrame = pd.DataFrame(topValues)
        risingValuesDataFrame = pd.DataFrame(risingValues)
        data = topValuesDataFrame
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")
        topSearchescollection.insert_many(data_dict)
        data1 = risingValuesDataFrame
        data1.reset_index(inplace=True)
        data_dict = data1.to_dict("records")
        risingSearchescollection.insert_many(data_dict)

except:
    print("ERROR in Related Queries")
# create collection for news (specific and related)
db.newssearchs.drop()
GoogleNewsSearchKeywordCollection = db['newssearchs']
db.newscategoryrelateds.drop()
GoogleNewsCategoryCollection = db['newscategoryrelateds']
googlenews = GoogleNews()
googlenews = GoogleNews('en', 'd')
keyword = ''

# using google news client to find specific news
try:
    googlenews.search(keywordToSearch)
    gnews = googlenews.result()
    gnewsDataFrame = pd.DataFrame(gnews)
    # gnewsDataFrame=gnewsDF.drop(['link', 'media', 'date'], axis=1)
    data = gnewsDataFrame.head(4)
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    GoogleNewsSearchKeywordCollection.insert_many(data_dict)
except:
    print("Error in specific category for News")


try:
    user_topic = user_category
    client = gnewsclient.NewsClient(language='english', location='', topic=user_topic, max_results=4)

    df = pd.DataFrame(client.get_news())
    x = df.drop(['link', 'media'], axis=1)
    data = x
    NewsCateogoryNews = data
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    GoogleNewsCategoryCollection.insert_many(data_dict)
except:
    print("No Goolge News")

# connect to Mongo DB Server
# client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
# connect to Mongo DB Server
client = MongoClient("mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/test?retryWrites=true&w=majority") #atlas


db = client.test  # test connection if connected
db = client[clientdatabaseName]  # open database if not available will be created

db.summarys.drop()  # delete collection to have fresh collection
summaryCollection = db['summarys']  # new collection for summary according to keyword

# find summary of keyword
keywordOne = keywordToSearch


# Check keyword if it contains multiple words
def contains_multiple_words(keywordOne):
    return len(keywordOne.split()) > 1


# if keyword contains multiple words tokenize and split for search
if contains_multiple_words(keywordOne) == True:
    word_tokens = nltk.word_tokenize(keywordOne)
    wordsWithPLus = ''
    for i in word_tokens:
        wordsWithPLus = wordsWithPLus + i + '+'
    keywordOne = wordsWithPLus
    keywordOne = keywordOne[:-1]

# code to get summary
try:  # try wikiAPI for summary
    keyword = keywordOne
    summary = wikipedia.summary(keyword, sentences=2)
    filteredList = []
    filteredList.append({'summary': summary})
    summaryCollection.insert_many(filteredList)
except:  # if not WikiAPI not availbe try Google Search
    query = keywordToSearch
    query = urllib.parse.quote_plus(query)  # Format into URL encoding
    number_result = 1

    ua = UserAgent()

    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)  # google search
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")

    result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})

    links = []  # links from search
    titles = []  # title fromm search
    descriptions = []  # description

    # find title links and description and append to list
    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href=True)
            title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()
            description = r.find('div', attrs={'class': 's3v9rd'}).get_text()

            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '':
                links.append(link['href'])
                titles.append(title)
                descriptions.append(description)
        # Next loop if one element is not present
        except:
            continue
    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa', l)

        # Anything that doesn't fit the above pattern will be removed
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))

    # Remove the corresponding titles & descriptions
    for x in to_remove:
        del titles[x]
        del descriptions[x]

    filteredList = []
    description_text = descriptions[0]
    filteredList.append({'summary': description_text})
    summaryCollection.insert_many(filteredList)
from datetime import datetime

dateTimeObj = datetime.now()
mostSearchedDateTimeStamp = most_Searched_Date.strftime("%Y-%m-%d")  # make most searched date to string

timestampStr = dateTimeObj.strftime("%Y-%m-%d")  # todays date
mostSearchedToToday = mostSearchedDateTimeStamp + " " + timestampStr  # creating timerange from most searched to today

pytrend.build_payload(kw_list=user_keyword_list, cat=0, timeframe=mostSearchedToToday, geo='')

interest_over_time = pytrend.interest_over_time()
df = pd.DataFrame(interest_over_time)
dfMost = pd.DataFrame(interest_over_time)
dataframeInterestOverTime1 = df.drop(['isPartial'], axis=1)
most_Searched_Date1 = dataframeInterestOverTime1[keywordToSearch].idxmax()  # most searched Date
most_Searched_Date12 = dataframeInterestOverTime1[keywordToSearch].idxmax()  # most searched Date

# convert timestamp to string
mostSearchedDateTimeStamp = most_Searched_Date1.strftime("%Y-%m-%d")
mostSearchedDateTimeStamp1=most_Searched_Date1.strftime("%d of %B %Y")  
mostSearchedwithoutDAte=most_Searched_Date1.strftime("%B %Y") 
predictEventDate = keywordToSearch + " " + mostSearchedwithoutDAte


my_dict = {'MostSearchedDate': mostSearchedDateTimeStamp1}  # create dictionary for most searched Date
db.mostsearcheddates.drop()  # send dictonary to mongoDB collection
mostsearchedDateCollection = db['mostsearcheddates']
mostsearchedDateCollection.insert_one(my_dict)

# code to find whether the keyword is trending now
try:
    import datetime

    currentTimestampStr = dateTimeObj.strftime("%Y-%m-%d")  # todays date
    datesforLastTenDays = []
    dates = [datetime.datetime.strptime(currentTimestampStr, '%Y-%m-%d') - datetime.timedelta(days=i) for i in
             range(600)]
    for day in dates:
        datesforLastTenDays.append(day.strftime('%Y-%m-%d'))

    tenDaysFeed = datesforLastTenDays[525] + " " + currentTimestampStr
    pytrend.build_payload(kw_list=user_keyword_list, cat=0, timeframe=tenDaysFeed, geo='')

    interest_over_time = pytrend.interest_over_time()
    df = pd.DataFrame(interest_over_time)
    dataframeInterestOverTime1 = df.drop(['isPartial'], axis=1)
    most_Searched_Date1 = dataframeInterestOverTime1[keywordToSearch].idxmax()  # most searched Date

    lastTenDaysDF=dataframeInterestOverTime1.tail(5)


    isItTrendingNow = ''
    if ((lastTenDaysDF > 80).any().bool()):
        isItTrendingNow = "YES"
    else:
        isItTrendingNow = "NO"

    maxValueLasytTenDays1=lastTenDaysDF.max()
    maxValueLasytTenDays=maxValueLasytTenDays1[0]
    
    int_value = int(maxValueLasytTenDays)
    print("Trending Now:", isItTrendingNow)
    mydictTrendingNow = {'trendingNow':int_value }  # creating dict for highest searched country
    db.isittrendingnows.drop()  # drop collection from db
    isItTrendingNowCollection = db['isittrendingnows']  # create collection
    isItTrendingNowCollection.insert_one(mydictTrendingNow)  # add to collection

except:
    mydictTrendingNow = {'trendingNow': 0}  # creating dict for highest searched country
    db.isittrendingnows.drop()  # drop collection from db
    isItTrendingNowCollection = db['isittrendingnows']  # create collection
    isItTrendingNowCollection.insert_one(mydictTrendingNow)  # add to collection
    print("NO")

# method to search using Google Custom Search and get titles
def google_CSE_Search():
    db = client[clientdatabaseName]
    from googleapiclient.discovery import build  # Import the library
    api_key = "AIzaSyBKoUBomRp30YqgVb9pB3MMcGsdU6A-36U"
    cse_id = "006943327039661084759:rfmkomnxylj"

    def google_query(query, api_key, cse_id, **kwargs):
        query_service = build("customsearch",
                              "v1",
                              developerKey=api_key
                              )
        query_results = query_service.cse().list(q=query,  # Query
                                                 cx=cse_id,  # CSE ID
                                                 **kwargs
                                                 ).execute()
        return query_results['items']

    my_results_links = []
    my_results_text = []
    my_results = google_query(predictEventDate,
                              api_key,
                              cse_id,
                              num=10
                              )
    my_dict_for_predicton = {}
    for result in my_results[:3]:
        my_results_links.append(result['link'])
        my_results_text.append(result['title'])
        title = result['title']
        title = title.replace(".", "")
        my_dict_for_predicton.update({title: result['link']})

    my_lst = my_results_text
    my_lst_str = ' '.join(map(str, my_lst))

    x = pd.DataFrame(my_dict_for_predicton.items(),
                     columns=['ID', 'Title'])  # add predicted event details to dataFrame
    data = x  # convert dataframe to dictionary
    predictedEventON = data
    data.reset_index(inplace=True)
    my_dict_for_predicton = data.to_dict("records")
    db = client[clientdatabaseName]  # make client database
    db.predictedevents.drop()  # drop table
    predictedEventCollection = db['predictedevents']  # create table
    predictedEventCollection.insert_many(my_dict_for_predicton)


# function to do useal google search and return resutls
def google_Search():
    from googlesearch import search
    query = predictEventDate
    my_dict_for_predicton = {}
    count = 0
    for j in search(query, tld="co.in", stop=3):
        my_dict_for_predicton.update({count: j, })
        count = count + 1
    x = pd.DataFrame(my_dict_for_predicton.items(),
                     columns=['ID', 'Title'])  # add predicited event details to dataframe
    data = x  # convert dataframe to dictonary
    predictedEventON = data
    data.reset_index(inplace=True)
    my_dict_for_predicton = data.to_dict("records")
    db = client[clientdatabaseName]  # make clinet database
    db.predictedevents.drop()  # drop table
    predictedEventCollection = db['predictedevents']  # create table
    predictedEventCollection.insert_many(my_dict_for_predicton)  # insert dictionary to mongodb collection


# if category is in the below list CSE [Custome Search Engine] will be used

CSE_search = ['politics', 'business', 'health']
predictedCountry = []
predictedCountryString = ''
CSE_search_true = 0
for word in CSE_search:
    if word == user_category:
        CSE_search_true = 1

if CSE_search_true == 1:
    try:
        google_CSE_Search()
    except:
        google_Search()

# using google to scrape results
else:
    google_Search()

my_dict = {'MostSearchedDate': mostSearchedDateTimeStamp1}  # create dictionary for most searched Date
db.mostsearcheddates.drop()  # send dictonary to mongoDB collection
mostsearchedDateCollection = db['mostsearcheddates']
mostsearchedDateCollection.insert_one(my_dict)

try:
    # using Youtbe Module to get youtbe Results
    try:
        from youtube_search import YoutubeSearch

        results = YoutubeSearch(keywordToSearch, max_results=4).to_json()
        Dict = eval(results)  # convert string to dictionary
        Dict['videos']
        youtuberesults = pd.DataFrame(Dict['videos'])

        data = youtuberesults
        data.reset_index(inplace=True)
        my_dict = data.to_dict("records")
    except:
        from youtube_search import YoutubeSearch

        results = YoutubeSearch(keywordToSearch, max_results=4).to_json()
        Dict = eval(results)
        Dict['videos']
        youtuberesults = pd.DataFrame(Dict['videos'])

        data = youtuberesults
        data.reset_index(inplace=True)
        my_dict = data.to_dict("records")
    else:
        print("")
except:
    print("YouTube Search Error")

try:
    db.youtuberesults.drop()
    youtubeCollection = db['youtuberesults']
    youtubeCollection.insert_many(my_dict)  # send youtube queries to collection
except:
    print("Cant find YouTUbe Data")

# get tweets for keyword
tweetsforKeyword = []  # empty list for tweets


# method to get tweets on keyword
def getTweetsForKeyword(text_query, count):
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=5):
            # Adding to list that contains all tweets
            tweetsforKeyword.append((tweet.created_at, tweet.id, tweet.text))

            # Creation of dataframe from tweets list
        tweetsdf = pd.DataFrame(tweetsforKeyword, columns=['Datetime', 'Tweet Id', 'Text'])
        data = tweetsdf
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")
        db = client[clientdatabaseName]  # make clinet database
        db.Tweets.drop()  # drop table
        tweetCollection = db['Tweets']  # create table
        tweetCollection.insert_many(data_dict)  # insert dictionary to mongodb collection
        print("Successfully Sent Tweets to DB")


    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


getTweetsForKeyword(keywordToSearch, 1)
