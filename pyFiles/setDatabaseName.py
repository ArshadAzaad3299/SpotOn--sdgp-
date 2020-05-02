
import pycountry
import sys

#Get Keyword passed from React to Node
userKeywordFromNode = sys.argv[1]


# keyword to Search + Category
keywordToSearch = userKeywordFromNode
for country in pycountry.countries:
    keywordToSearch = keywordToSearch.title()
    if country.name in keywordToSearch:
        keywordToSearch = keywordToSearch.title()
        break
    else:
        keywordToSearch = keywordToSearch.lower()

clientdatabaseName = keywordToSearch.replace(" ", "")


sys.stdout.write(clientdatabaseName)

