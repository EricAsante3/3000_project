# if you get some error talking bout stopwords run /Applications/Python\ 3.13/Install\ Certificates.command in terminal


import pandas as pnd
import nltk
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from scipy.sparse import hstack
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


csv = pnd.read_csv("./labeled_data.csv")



nltk.download("stopwords")
stpwrd = set(stopwords.words("english"))

def preProcessText(txt):
  words = txt.lower().split()
  words = [word for word in words if word.isalpha() and word not in stpwrd]
  return " ".join(words)

csv["tweet"] = csv["tweet"].astype(str).apply(preProcessText)


vectorizer = TfidfVectorizer()
xtweet = vectorizer.fit_transform(csv["tweet"])


xother = csv[["count", "hate_speech", "offensive_language", "neither", "class"]].values if "count" in csv else None

x = hstack((xtweet, xother)) if xother is not None else xtweet

y = LabelEncoder().fit_transform(csv["class"])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(xtrain, ytrain)

ypred = model.predict(xtest)

accuracy = accuracy_score(ytest, ypred)

def predictClassification(tweet):
  processedText = preProcessText(tweet)
  textFeatures = vectorizer.transform([processedText])
  combinedFeatures = hstack((textFeatures, np.array([[0, 0, 0, 0, 0]]))) if xother is not None else textFeatures
  predict = model.predict(combinedFeatures)
  return "Hate Speech" if predict[0] == 0 else "Offensive Language" if predict[0] == 1 else "Neither"


def test(input):
    return [accuracy,classification_report(ytest, ypred),predictClassification(input)]


