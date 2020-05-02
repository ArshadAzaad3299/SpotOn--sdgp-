
from pytrends.request import TrendReq
import datetime
from datetime import date
from datetime import datetime
import pandas as pd
import sys

userKeywordFromNode = sys.argv[1]
keywordToSearch = userKeywordFromNode
user_keyword_list = [keywordToSearch]

try:
    pytrend = TrendReq()
except:
    pytrend = TrendReq()


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
# searchedCountryCollection.insert_many(data_dict)  # insert to Database
df = pd.DataFrame(data_dict)
countryNames = df['geoName'].tolist()
values = df['name'].tolist()

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(9,5))
fig=plt.rcParams['axes.facecolor'] = '#3A3E46'

COLOR = 'white'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR

objects = countryNames
y_pos = np.arange(len(objects))
performance = values

plt.bar(y_pos, performance, align='center', alpha=0.5, color=('#A3A1FB'))
plt.xticks(y_pos, objects,rotation=90)
plt.ylabel('Search Percentage')
plt.title('Total Searches By Country')
plt.savefig('./client/src/components/result-component/searchedcountry.png',transparent=True)
# plt.savefig('searchedcountry.png',transparent=True)

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
for x in dates:
    line = str(x)
    time_object = datetime.strptime(line, '%Y-%m-%d %H:%M:%S').date()
    d = time_object.strftime("%m/%d")
    datesupdated.append(d)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(19,6))
fig=plt.rcParams['axes.facecolor'] = '#3A3E46'

COLOR = 'white'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR

objects = datesupdated
y_pos = np.arange(len(objects))
performance = values

plt.plot(y_pos, performance, color=('#A3A1FB'))
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Search Percentage')
plt.title('Searches for Last 15 Years')
plt.savefig('./client/src/components/result-component/searcheddates.png',transparent=True)




