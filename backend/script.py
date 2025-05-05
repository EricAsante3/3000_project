# if you get some error talking bout stopwords run /Applications/Python\ 3.13/Install\ Certificates.command in terminal

# import all libraries -- if things don't work refer to requirements.txt. Try running the files in a virtual environment (venv)
# with the latest version of python. Venv should download the dependencies automatically, but if it fails,
# you may need to run 'pip install {library}' on the venv interpreter
import pandas as pnd
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from scipy.sparse import hstack
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# import dataset using pandas
csv = pnd.read_csv("dataset.csv")


# imports nltk stopwords database for pre-processing
nltk.download("stopwords")
stpwrd = set(stopwords.words("english"))

# preProcessText function simplifies all data input and removes special characters and certain things that may affect reading
# returns a new string with capitalization and extra symbols removed
def preProcessText(txt):
  words = txt.lower().split()
  words = [word for word in words if word.isalpha() and word not in stpwrd]
  return " ".join(words)

# runs preProcessText function on all entries in dataset
csv["tweet"] = csv["tweet"].astype(str).apply(preProcessText)

# initialize vectorizer for dataset, assigns a vector per entry
vectorizer = TfidfVectorizer()
xtweet = vectorizer.fit_transform(csv["tweet"])

# reads csv classifiers from dataset for interpretation
xother = csv[["count", "hate_speech", "offensive_language", "neither", "class"]].values if "count" in csv else None

x = hstack((xtweet, xother)) if xother is not None else xtweet

y = LabelEncoder().fit_transform(csv["class"])

# run training algorithm from library
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# initializes multinomial naive-bayes model for training and classification
model = MultinomialNB()
model.fit(xtrain, ytrain)

# run predictions for accuracy test
ypred = model.predict(xtest)

accuracy = accuracy_score(ytest, ypred)


# takes string input and performs preprocessing before submission to the NB model for predicted classification
# return values:
# 0 = hate speech
# 1 = offensive language 
# 2 = neither
def predictClassification(tweet):
  processedText = preProcessText(tweet)
  textFeatures = vectorizer.transform([processedText])
  combinedFeatures = hstack((textFeatures, np.array([[0, 0, 0, 0, 0]]))) if xother is not None else textFeatures
  predict = model.predict(combinedFeatures)
  return "Hate Speech" if predict[0] == 0 else "Offensive Language" if predict[0] == 1 else "Neither"

# generate classification report
report = classification_report(ytest, ypred)
print(str(report))

def plot():
    dreport = classification_report(ytest, ypred, output_dict=True)
    classes = list(dreport.keys())[:-3]
    precision = [dreport[class_name]['precision'] for class_name in classes]
    recall = [dreport[class_name]['recall'] for class_name in classes]

    x = np.arange(len(classes))
    width = .35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, precision, width, label='Precision', color='b')
    ax.bar(x + width/2, recall, width, label='Recall', color='g')

    ax.set_xlabel('Classes')
    ax.set_ylabel('Scores')
    ax.set_title('Precision and Recall for Each Class')
    ax.set_xticks(x)
    ax.set_xticklabels(classes)
    ax.legend()
    
    plt.show()

# accept user input and return it into docker
def test(input):
    return [accuracy,report,predictClassification(input)]




