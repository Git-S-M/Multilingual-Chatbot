import sklearn
import pickle
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
 
 
def predict(text):
    # loading the dataset
    data = pd.read_csv("language_detection.csv")
    y = data["Language"]

    # label encoding
    y = le.fit_transform(y)

    #loading the model and cv
    model = pickle.load(open("model.pkl", "rb"))
    cv = pickle.load(open("transform.pkl", "rb"))
    
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', '', text)
    text = re.sub(r'[[]]', '', text)
    text = text.lower()
    dat = [text]
    # creating the vector
    vect = cv.transform(dat).toarray()
    # prediction
    my_pred = model.predict(vect)
    my_pred = le.inverse_transform(my_pred)

    return my_pred[0]



