import pickle
import os
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import TfidfVectorizer
from random import randint
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import pymongo
from pymongo import MongoClient
# client =MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")

# connect to Mongo DB Server
client = MongoClient("mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/test?retryWrites=true&w=majority") #atlas


db = client.test  # test connection if connected

db = client['newscategory']     #open database if not available will be created
TRAIN_MODEL_PATH = os.path.join("../FrontEnd/pyFiles/input/", "NewsTrain1.csv")
df = pd.read_csv(TRAIN_MODEL_PATH)
# Associate Category names with numerical index and save it in new column category_id
df['category_id'] = df['Category'].factorize()[0]
category_id_df = df[['Category', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Category']].values)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

features = tfidf.fit_transform(df.Text).toarray() # Remaps the words in the 1490 articles in the text column of 
                                                  # data frame into features (superset of words) with an importance assigned 
                                                  # based on each words frequency in the document and across documents
filename = '../FrontEnd/pyFiles/input/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

texts = []
# importing requests package 
import requests      
  
def NewsFromBBC():
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
# fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
# getting all articles in a string article 
    article = open_bbc_page["articles"] 
# empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        texts.append(ar["title"]) 
                      
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  

#create list to append news after categorizing
sportLists=[]
techList=[]
entertainmentList=[]
healthList=[]
businessList=[]
politicsList=[]

#categorizing news based on topics
#And appending to list and declared Above
text_features = tfidf.transform(texts)
predictions = loaded_model.predict(text_features)
for text, predicted in zip(texts, predictions):
    
    if format(id_to_category[predicted])=='sport':
        sportText=format(text)
        sportLists.append(sportText)
    elif format(id_to_category[predicted])=='politics':
        politcsText=format(text)
        politicsList.append(politcsText)
    elif format(id_to_category[predicted])=='business':
        businessText=format(text)
        businessList.append(businessText)
    elif format(id_to_category[predicted])=='entertainment':
        entertainmentText=format(text)
        entertainmentList.append(entertainmentText)
    elif format(id_to_category[predicted])=='health':
        healthText=format(text)
        healthList.append(healthText)
    elif format(id_to_category[predicted])=='tech':
        techText=format(text)
        techList.append(techText)


# Establishing connection to MongoDB


#Health DB
healthCollection = db['healths']  # new collection for Health news according to Category

#Politics DB
politicsCollection = db['politics']  # new collection for Health news according to Category

#techs DB
techsCollection = db['techs']  # new collection for Health news according to Category

#Entertainment DB
entertainmentCollection = db['entertainments']  # new collection for Health news according to Category

#Business DB
# db.business.drop()  # delete collection to have fresh collection
businessCollection = db['business']  # new collection for Health news according to Category

#Sport DB
sportsCollection = db['sports']  # new collection for Health news according to Category

#create dictionary and Dataframe
businessListDict={}
column_names = ['Text']

businessdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
sportsListDict={}
sportsdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
entertainmentListDict={}
entertainmentdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
politicsListDict={}
politicsdf = pd.DataFrame(columns = column_names)

#create dictionary and Dataframe
healthListDict={}
healthdf = pd.DataFrame(columns = column_names)
#create dictionary and Dataframe

techListDict={}
techdf = pd.DataFrame(columns = column_names)

#iterate through list and append to dataframe then to list and then send to DB
if len(businessList)!=0:
    for item in businessList:
        businessdf = businessdf.append({'Text': item}, ignore_index=True)
    data = businessdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    businessCollection.insert_many(data_dict)
else:
    print('empty list of businessList')

    
#iterate through list and append to dataframe then to list and then send to DB
if len(sportLists)!=0:
    for item in sportLists:
        sportsdf = sportsdf.append({'Text': item}, ignore_index=True)
    data = sportsdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    sportsCollection.insert_many(data_dict)
else:
    print('empty list of sportsList')
    
#iterate through list and append to dataframe then to list and then send to DB
if len(techList)!=0:
    for item in techList:
        techdf = techdf.append({'Text': item}, ignore_index=True)
    data = techdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    techsCollection.insert_many(data_dict)
else:
    print('empty list of tech')
    
#iterate through list and append to dataframe then to list and then send to DB
if len(entertainmentList)!=0:
    for item in entertainmentList:
        entertainmentdf = entertainmentdf.append({'Text': item}, ignore_index=True)
    data = entertainmentdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    entertainmentCollection.insert_many(data_dict)
else:
    print('empty list of entertainment')
    
#iterate through list and append to dataframe then to list and then send to DB
if len(politicsList)!=0:
    for item in politicsList:
        politicsdf = politicsdf.append({'Text': item}, ignore_index=True)
    data = politicsdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    politicsCollection.insert_many(data_dict)
else:
    print('empty list of politicsCollection')

#iterate through list and append to dataframe then to list and then send to DB
if len(healthList)!=0:
    for item in healthList:
        healthdf = healthdf.append({'Text': item}, ignore_index=True)
    data = healthdf
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    healthCollection.insert_many(data_dict)
else:
    print('empty list of Health')

