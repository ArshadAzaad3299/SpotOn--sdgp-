import os
import RelatedSearches
import enchant
import pandas as pd
import tweepy
import json
from pymongo import MongoClient


d = enchant.Dict("en_US")



# Authentication to twitter
# Complete authorization and initialize API endpoint
auth = tweepy.OAuthHandler("OVTdS84lJEILeeldhGCUZYNqg", "6QRG9zAdezggILyzPcKH2wzpSHqmpsKSlNXTTPMADrGVQ6lKLr")
auth.set_access_token("405223959-hQfJbDlma2vxkF1YKVvOjFDhJPTIdLnxoNkmiipk",
                      "d18NNIPXQ3yixNB6j0bgaJ6ib6aAz8oHcP0TfmmABfbzn")

api = tweepy.API(auth, wait_on_rate_limit=True)

# test authentication
try:
    api.verify_credentials()
    print("Authentication - SUCCESSFUL")
except:
    print("Error during authentication")

# Defining the search term and the date_since date as variables
# search_word_list = ["#ronaldo", "#Sports", "#realmadrid"]
# related_searches_list = RelatedSearches.related_searches_list
# search_word_list = related_searches_list
date_since = "2019-10-16"


# Function which is used to extract tweets and return the results as a data frame
def collectTweets(keyword_to_search):
    tweets = tweepy.Cursor(api.search, q=keyword_to_search, lan="en", since=date_since).items(50)
    # Gathering extracted data into python data frame
    extractedTweetsDataFrame = pd.DataFrame(pd.DataFrame(t.__dict__ for t in tweets))
    return extractedTweetsDataFrame;

##############################################################
def tweetScrapeFunction(search_word_list,user_searched_phrase):
    # Creating an empty list which will store the data frames in it
    frames = []
    for i in search_word_list:
        df = (collectTweets(i))
        frames.append(df)  # Storing the Data frame in the list "frames"

    # Concatenating All the Data frames in the list "frames" and storing it in another Data frame "result"
    result = pd.concat(frames)

    # Calculating the number of rows in the data frame
    number_of_rows = result['text'].count()

    # Checking if the number of rows are correctly stored (By printing on the console)
    # print(number_of_rows)

    # Rearranging the index of the data frame "result" beginning from 0 to ........
    result.index = range(number_of_rows)

    # Extracting only the text, retweet_count, lang from the results and storing in a data frame "newlyFormedTweetsDataaFrame"
    newlyFormedTweetsDataaFrame = result[['text', 'retweet_count', 'lang']].copy()

    # step_01_filtered_DataFrame =>  here the language 'en' tweets are only selected and stored in this Data frame
    step_01_filtered_DataFrame = newlyFormedTweetsDataaFrame[(newlyFormedTweetsDataaFrame['lang'] == 'en')]

    # Removing Non-English Words From the Extracted tweet text
    for i, row in step_01_filtered_DataFrame.iterrows():
        full = ""  # an empty string
        # storing the value of 'text' in the (i) position of the step_01_filtered_DataFrame to the variable x
        x = step_01_filtered_DataFrame['text'][i]
        # Iterating over the String x, and storing only the valid terms in to the variable "full"
        for j in x:
            if ((d.check(j)) == True):
                full += j
            else:
                continue
        # Changing the value of column 'text' as value in variable 'full'
        step_01_filtered_DataFrame._set_value(i, 'text', full)

    # step_01_filtered_DataFrame.to_csv(r'step_01_filtered_DataFrame.csv')
    # indexNameLang = new[new['lang'] == 'en'].index
    # new.drop(indexNameLang, inplace=True)
    # print(new)

    # Initially Removing all the files in the folder
    # dir_name = ('E:\Studies\Give A Try\SDGP\Data Set\\Test BBC\\business')
    dir_name = ('./pyFiles/TextClassificationPhase_01/Test BBC/business')
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".txt"):
            os.remove(os.path.join(dir_name, item))

    # Writing the final tweets to txt files
    count = 0
    finalListOnlyWithText = []
    for i, row in step_01_filtered_DataFrame.iterrows():
        x = step_01_filtered_DataFrame['text'][i]
        finalListOnlyWithText.append(x)
        filename = str(count) + "dataFile.txt"
        # file1 = open("E:\Studies\Give A Try\SDGP\Data Set\Test BBC\\business\\" + filename + "", "w")
        file1 = open("./pyFiles/TextClassificationPhase_01/Test BBC/business/" + filename + "", "w")
        file1.writelines(x)
        count += 1
        file1.close()
    onlyTextDF = pd.DataFrame(finalListOnlyWithText)
    onlyTextDF['index'] = range(1, len(onlyTextDF)+1)
    onlyTextDF=onlyTextDF.rename(columns={0:"text"})

    user_searched_phrase = user_searched_phrase.replace(" ", "")



    #Save All tweets to Database
    client = MongoClient("mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/test?retryWrites=true&w=majority")
    mydb = client[user_searched_phrase]
    mycol = mydb["Tweets"]
    mycol.drop()
    print(onlyTextDF)

    records = json.loads(onlyTextDF.T.to_json()).values()
    mycol.insert_many(records)



    # Calculating the number of rows in the data frame
    number_of_rows = step_01_filtered_DataFrame['text'].count()

    # Checking if the number of rows are correctly stored (By printing on the console)
    # print(number_of_rows)