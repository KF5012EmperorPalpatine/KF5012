from dataProcess import dataProcess
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def predict(corpus):
    predictor = pickle.load(open("finalised_model.sav","rb"))
    vectorizer = pickle.load(open("vectorizer.sav","rb"))
    prediction = predictor.predict(vectorizer.transform(corpus))[0]
    return prediction