from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from dataProcess import dataProcess

#Pre process data. See module file dataProcess.py for details
corpus, labels = dataProcess("DJIA.csv")
countVect = CountVectorizer(ngram_range=(2, 2))
dataset = countVect.fit_transform(corpus)

# split the data into training and testing
x_train, x_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.3, shuffle=False)

#create SVM classifier
print('Classification method: SVM')
SVM = svm.SVC(kernel='linear', C=10)
SVM.fit(x_train, y_train)
#predict classes and print results
y_pred = SVM.predict(x_test)
confmat = confusion_matrix(y_test, y_pred)
print("here")
print(confmat)
acc = accuracy_score(y_test, y_pred)
print(acc)
print('\n')


pickle.dump(countVect,open('vectorizer.sav','wb'))
pickle.dump(SVM,open('finalised_model.sav','wb'))
