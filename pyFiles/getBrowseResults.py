import sys
import nltk
import numpy as np
import sys
from pandas import DataFrame
import pandas as pd
from random import randint

#get variable from node
user_get = sys.argv[1]

#Establishing connection to MongoDB
import pymongo
from pymongo import MongoClient
# client = MongoClient("localhost", 27017, maxPoolSize=50)
# connect to Mongo DB Server
client = MongoClient("mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/test?retryWrites=true&w=majority") #atlas


db = client.test  # test connection if connected

user_preferences=user_get
user_preferences = user_preferences.replace(',', ' ')
word_tokens= nltk.word_tokenize(user_preferences)
word_tokens

mydb = client["browse"]
mydb.newsdatas.drop()  

#if sports exists in user preferences get news from sports database and add to user required Db
try:
    if 'sports' in word_tokens:
        mydb = client["newscategory"]
        mycol = mydb["sports"]
        x = mycol.find()
        myList=[]
        column_names = ['ArticleId', 'Text']  #column names for DataFrame
        df = pd.DataFrame(columns = column_names)  #create DataFrame

        for x in mycol.find({},{"Text":1,"_id": False}):
            #code to remove unnecessary characters from string
            strx=str(x)
            string=strx
            string=string
            string=string.replace("Text","")
            string=string.replace("''","")
            string=string.replace("{","")
            string=string.replace("}","")
            string=string.replace(":","")
            string=string.replace("'","")
            string=string.replace("","")
            myList.append(string)
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)
        for item in myList:
            value = randint(10, 90)
            df = df.append({'ArticleId': value, 'Text': item}, ignore_index=True)
        df = df.sample(n=4)
        mydb = client["browse"]
        data=df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")

        mydb = client["browse"]
        newscollection = mydb['newsdatas']   #new collection for top searches 
        newscollection.insert_many(data_dict)
        
except:
    print("No Sports News")
    
#if space exists in user preferences get news from sports database and add to user required Db
try:
    if 'space' in word_tokens:
        mydb = client["newscategory"]
        mycol = mydb["space"]
        x = mycol.find()
        myList=[]
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)

        for x in mycol.find({},{"Text":1,"_id": False}):

            strx=str(x)
            string=strx
            string=string
            string=string.replace("Text","")
            string=string.replace("''","")
            string=string.replace("{","")
            string=string.replace("}","")
            string=string.replace(":","")
            string=string.replace("'","")
            myList.append(string)
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)
        for item in myList:
            value = randint(100, 150)
            df = df.append({'ArticleId': value, 'Text': item}, ignore_index=True)
        df = df.sample(n=4)
        mydb = client["browse"]
        data=df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")

        mydb = client["browse"]
        newscollection = mydb['newsdatas']   #new collection for top searches 
        newscollection.insert_many(data_dict)
    else:
        print("News Collection Empty")
        
except:
    print("No Space")

#if politics exists in user preferences get news from sports database and add to user required Db
try:
    if 'politics' in word_tokens:
        mydb = client["newscategory"]
        mycol = mydb["politics"]
        # "_id": False
        x = mycol.find()
        myList=[]
        myDict={}
        count=0
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)

        for x in mycol.find({},{"Text":1,"_id": False}):
            strx=str(x)
            string=strx
            string=string
            string=string.replace("Text","")
            string=string.replace("''","")
            string=string.replace("{","")
            string=string.replace("}","")
            string=string.replace(":","")
            string=string.replace("'","")
            myList.append(string)
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)
        for item in myList:
            value = randint(200, 250)
            df = df.append({'ArticleId': value, 'Text': item}, ignore_index=True)
        df = df.sample(n=4)
        mydb = client["browse"]
        data=df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")

        mydb = client["browse"]
        newscollection = mydb['newsdatas']   #new collection for top searches 
        newscollection.insert_many(data_dict)
        
except:
    print("No politics")
    
#if haelth exists in user preferences get news from sports database and add to user required Db
try:
    if 'health' in word_tokens:
        mydb = client["newscategory"]
        mycol = mydb["health"]
        # "_id": False
        x = mycol.find()
        myList=[]
        myDict={}
        count=0
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)

        for x in mycol.find({},{"Text":1,"_id": False}):
            print(x)
            strx=str(x)
            string=strx
            string=string
            string=string.replace("Text","")
            string=string.replace("''","")
            string=string.replace("{","")
            string=string.replace("}","")
            string=string.replace(":","")
            string=string.replace("'","")
            myList.append(string)
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)
        for item in myList:
            value = randint(300, 350)
            df = df.append({'ArticleId': value, 'Text': item}, ignore_index=True)
        df = df.sample(n=4)
        mydb = client["browse"]
        data=df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")

        mydb = client["browse"]
        newscollection = mydb['newsdatas']   #new collection for top searches 
        newscollection.insert_many(data_dict)
        
except:
    print("No health")
    
#if entertainment exists in user preferences get news from sports database and add to user required Db
try:
    if 'entertainment' in word_tokens:
        mydb = client["newscategory"]
        mycol = mydb["entertainment"]
        # "_id": False
        x = mycol.find()
        myList=[]
        myDict={}
        count=0
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)

        for x in mycol.find({},{"Text":1,"_id": False}):
            print(x)
            strx=str(x)
            string=strx
            string=string
            string=string.replace("Text","")
            string=string.replace("''","")
            string=string.replace("{","")
            string=string.replace("}","")
            string=string.replace(":","")
            string=string.replace("'","")
            myList.append(string)
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)
        for item in myList:
            value = randint(500, 550)
            df = df.append({'ArticleId': value, 'Text': item}, ignore_index=True)
        df = df.sample(n=4)
        mydb = client["browse"]
        data=df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")

        mydb = client["browse"]
        newscollection = mydb['newsdatas']   #new collection for top searches 
        newscollection.insert_many(data_dict)
        
except:
    print("No Entertainment")
    
#if business exists in user preferences get news from sports database and add to user required Db
try:
    if 'business' in word_tokens:
        mydb = client["newscategory"]
        mycol = mydb["business"]
        # "_id": False
        x = mycol.find()
        myList=[]
        myDict={}
        count=0
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)

        for x in mycol.find({},{"Text":1,"_id": False}):
            print(x)
            strx=str(x)
            string=strx
            string=string
            string=string.replace("Text","")
            string=string.replace("''","")
            string=string.replace("{","")
            string=string.replace("}","")
            string=string.replace(":","")
            string=string.replace("'","")
            myList.append(string)
        column_names = ['ArticleId', 'Text']
        df = pd.DataFrame(columns = column_names)
        for item in myList:
            value = randint(400, 450)
            df = df.append({'ArticleId': value, 'Text': item}, ignore_index=True)
        df = df.sample(n=4)
        mydb = client["browse"]
        data=df
        data.reset_index(inplace=True)
        data_dict = data.to_dict("records")
        mydb = client["browse"]
        newscollection = mydb['newsdatas']   #new collection for top searches 
        newscollection.insert_many(data_dict)
        
except:
    print("No Business")



