import smtplib
import sys
from pymongo import MongoClient
import pymongo
from pandas import DataFrame
import pandas as pd
import pymongo
from random import randint

from pymongo import MongoClient
# client = MongoClient("localhost", 27017, maxPoolSize=50)

#mongodb Atlas
client =MongoClient('mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/whatIsSearchedToday?authSource=admin&replicaSet=sdgp1-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true')

db = client.test  # test connection if connected

#Get Keyword passed from React to Node
useremail = sys.argv[1]
mydb = client["whatIsSearchedToday"]
mycol = mydb["whatissearchedtodays"]
x = mycol.find()
myList=[]
column_names = ['ArticleId', 'query']  #column names for DataFrame
df = pd.DataFrame(columns = column_names)  #create DataFrame

for x in mycol.find({},{"query":1,"_id": False}):
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
#     string=string.replace("query","topic:")
    string=string.replace("","")
    myList.append(string)
column_names = ['ArticleId', 'Text']
df = pd.DataFrame(columns = column_names)

messageFromList=(" \n".join(myList))

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "spotonsdgp@gmail.com"
receiver_email = useremail
message = messageFromList

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, 'sdgp1234')
    server.sendmail(sender_email, receiver_email, message)


    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
