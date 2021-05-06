# import and download required libraries
import numpy
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import svm
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle

# read the data
dataframe = pd.read_csv('DJIA.csv')

# split data into features (headlines/corpus) and labels (stock movement classified as up and down)
dataframe['Headlines'] = dataframe[dataframe.columns[2:]].apply(lambda x: '. '.join(x.dropna().astype(str)), axis=1)
corpus = dataframe['Headlines']
labels = dataframe['Label']

# remove punctuation and make lowercase
corpus.replace("[^a-zA-Z]", " ", regex=True, inplace=True)
corpus = corpus.str.lower()

# calculate the sentiment value for each line (all news of a day)
sia = SentimentIntensityAnalyzer()
results = []  # will contain the compound score
for line in corpus:
    pol_score = sia.polarity_scores(line)
    results.append(pol_score)
# results

# move the results to 'score', add them to dataframe and see the correlation
score = pd.DataFrame(results)['compound']
print('Correlation between the price movement and sentiment of the day')
print(score.corr(labels))
print('\n')
dataframe['Sentiment Score'] = score

# convert the datatypes so it can be worked with them later
corpus = corpus.tolist()
labels = labels.to_numpy()

# text representation: bag of words approach with count vectorizer (bigrams)
print('Word representation method: Bag of Words using Count Vectorizer')
countVect = CountVectorizer(ngram_range=(2, 2))
dataset = countVect.fit_transform(corpus)

# split the data into training and testing
x_train, x_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.3, shuffle=False)

#create SVM classifier
print('Classification method: SVM')
SVM = svm.SVC(kernel='linear', C=10)
SVM.fit(x_train, y_train)

#predict classes and print results
print('Performance')
y_pred = SVM.predict(x_test)
confmat = confusion_matrix(y_test, y_pred)
<<<<<<< HEAD
print("here")
=======
print('Confusion Matrix')
>>>>>>> model
print(confmat)
print('\n')
<<<<<<< HEAD

filename = 'finalised_model.sav'
pickle.dump(SVM,open(filename,'wb'))

#text representation: bag of words using tfidf (bigrams)
print('Word representation method: Bag of Words using TFIDF Vectorizer')
tfidf = TfidfVectorizer(ngram_range=(2,2))
dataset = tfidf.fit_transform(corpus)

# split the data into training and testing
x_train, x_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.3, shuffle=False)

#create naive bayes model
print('Classification method: Naive Bayes')
naive = MultinomialNB()
naive.fit(x_train, y_train)
#predict classes and print results
y_pred = naive.predict(x_test)
confmat = confusion_matrix(y_test, y_pred)
print(confmat)
=======
>>>>>>> model
acc = accuracy_score(y_test, y_pred)
print('Accuracy (%) on testing dataset')
print(acc*100)

y_pred = SVM.predict(x_train)
acc = accuracy_score(y_train, y_pred)
print('Accuracy (%) on training dataset')
print(acc*100)
print('\n')
