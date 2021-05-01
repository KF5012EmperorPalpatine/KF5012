#import and download required libraries
from numpy import array
from keras.preprocessing.text import one_hot, Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, LSTM
from keras.layers.embeddings import Embedding
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('all')

#read the data
dataframe = pd.read_csv('DJIA.csv')
dataframe.head()

#split data into features (headlines/corpus) and labels (stock movement classified as up and down)
dataframe['Headlines'] = dataframe[dataframe.columns[2:]].apply(lambda x: '. '.join(x.dropna().astype(str)),axis=1)
corpus = dataframe['Headlines']
labels = dataframe['Label']
#remove punctuation and make lowercase
corpus.replace("[^a-zA-Z]", " ", regex=True, inplace=True) 
corpus = corpus.str.lower()

#calculate the sentiment value for each line (all news of a day)
sia = SentimentIntensityAnalyzer()
results = [] #will contain the compound score
for line in corpus:
  pol_score = sia.polarity_scores(line)
  results.append(pol_score)
#results

#move the results to a dataframe and see the correlation
score = pd.DataFrame(results)['compound']
score.corr(labels)

#convert the datatypes so it can be worked with them later
corpus =  corpus.tolist()
labels = labels.to_numpy()

#set the stop words (including the leading 'b' which appears in some sentences)
stop_words = set(nltk.corpus.stopwords.words('english'))
stop_words.add("b")

#remove stop words 
corpus_without_sw = []
for sent in corpus:
  sent_tokens = word_tokenize(sent)
  tokens_without_sw = [w for w in sent_tokens if not w in stop_words]
  filtered_sent = (" ").join(tokens_without_sw)
  #print(filtered_sent)
  corpus_without_sw.append(filtered_sent)

#tokenize the corpus 
word_tokenizer = Tokenizer()
word_tokenizer.fit_on_texts(corpus_without_sw)

#get the vocabulary length which is used in the first layer of the model
vocab_length = len(word_tokenizer.word_index) +1

#convert all the sentences (lines) in corpus to numeric arrays 
embedded_sentences = word_tokenizer.texts_to_sequences(corpus_without_sw)
#print(embedded_sentences)

#get size of the largest line (in number of words) and pad the other lines with zeros at the end until they reach that size
word_count = lambda sentence: len(word_tokenize(sentence))
longest_sentence = max(corpus_without_sw, key=word_count)
length_long_sentence = len(word_tokenize(longest_sentence))

padded_sentences = pad_sequences(embedded_sentences, length_long_sentence, padding='post')
#print(padded_sentences)

#split the data into training and testing
x_train, x_test, y_train, y_test = train_test_split(padded_sentences, labels, test_size=0.3)

#create a model
model = LinearDiscriminantAnalysis()

#fit training data to the model
model.fit(x_train, y_train)

#predict test y values using
y_pred = model.predict(x_test)

#calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred) * 100
print(accuracy)