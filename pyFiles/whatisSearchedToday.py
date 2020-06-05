from pymongo import MongoClient
import pymongo
import pandas as pd
from pytrends.request import TrendReq

#connect to Mongo DB Server
# client =MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")

#mongodb Atlas
client =MongoClient('mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/whatIsSearchedToday?authSource=admin&replicaSet=sdgp1-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')

db = client.test             #test connection if connected

#establishing connection with google trends

try:
    pytrend = TrendReq()
except:
    pytrend = TrendReq()
clientdatabaseName='whatIsSearchedToday'
today_searches_df = pytrend.today_searches()
db = client[clientdatabaseName]     #open database if not available will be created
db.whatissearchedtodays.drop()            #delete collection to have fresh collection
whatIsSearchedTodayCollection = db['whatissearchedtodays']   #new collection for what is searched today
df=pd.DataFrame(today_searches_df)
try:
    df=df.head(6)
except:
    print("Less Than 6 values")

#Convert DataFrame to Dictionary and send values to MongoDb Collection
data=df
whatIsSearchedToday=data
data.reset_index(inplace=True)
data_dict = data.to_dict("records")
whatIsSearchedTodayCollection.insert_many(data_dict)