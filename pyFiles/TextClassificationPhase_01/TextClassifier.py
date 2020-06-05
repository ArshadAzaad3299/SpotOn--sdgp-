import pickle

import sklearn.datasets as skd

categories = ['business', 'entertainment', 'politics', 'sport', 'tech', 'space', 'health_environment']
print()
news_train = skd.load_files('/Data Set/News & BBC', categories=categories,
                            encoding='ISO-8859-1')
news_test = skd.load_files('/Data Set/News & BBC', categories=categories,
                           encoding='ISO-8859-1')

# # Step - 05 => Training and Testing Sets
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

text_clf = Pipeline([('vect', TfidfVectorizer()),
                     ('clf', MultinomialNB())])

# train the model
text_clf.fit(news_train.data, news_train.target)
# Predict the test cases
predicted = text_clf.predict(news_test.data)
print(news_train['target_names'])
print(predicted)

from sklearn import metrics
import numpy as np

print('Accuracy achieved is ' + str(np.mean(predicted == news_test.target)))
print(metrics.classification_report(news_test.target, predicted, target_names=news_test.target_names)),
metrics.confusion_matrix(news_test.target, predicted)

# saving to a pickle file
with open('text_classifier_model', 'wb') as picklefile:
    pickle.dump(text_clf, picklefile)
