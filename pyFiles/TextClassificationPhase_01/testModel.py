import os
import pickle

import sklearn.datasets as skd
# import RelatedSearches
# import tweetScrapeAndSave

# news_test = skd.load_files('E:\Studies\Give A Try\SDGP\Data Set\\Test BBC', encoding='ISO-8859-1')
news_test = skd.load_files('./pyFiles/TextClassificationPhase_01/Test BBC', encoding='ISO-8859-1')
# print(news_test['target_names'])
listOfTopics = news_test['target_names']

# Importing the trained model
with open('./pyFiles/TextClassificationPhase_01/text_classifier_model', 'rb') as training_model:
    model = pickle.load(training_model)

final_result = []
try:
    # x = (model.predict(news_test.data))[0]
    x = model.predict(news_test.data)
    # print(x)
    for i in x:
        final_result.append(listOfTopics[i])
        # print(listOfTopics[i])
    # print(listOfTopics[x])
except:
    print("SOME ERROR OCCURRED")

# print(final_result)
# Finding the maximum occur in the list
try:
    final_result_achieved = max(final_result, key=final_result.count)
except:
    final_result_achieved = "SOME ERROR OCCURRED"
# print(final_result_achieved)

# After the final result is stored the .txt files are removed
dir_name = ('./pyFiles/TextClassificationPhase_01/Test BBC/business')
test = os.listdir(dir_name)
for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))
