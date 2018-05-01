#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
# your code goes here ###

"""
training time: 170.885 s
predict time: 16.963 s
predict result ->  [0 0 1 ... 1 0 0]
accuracy ->  0.9840728100113766
"""
# clf = SVC(kernel="linear")
# t0 = time()
# clf.fit(features_train, labels_train)
# print "training time:", round(time()-t0, 3), "s"
# t0 = time()
# pred = clf.predict(features_test)
# print "predict time:", round(time()-t0, 3), "s"
#
# print "predict result -> ", pred
#
# print "accuracy -> ", accuracy_score(pred, labels_test)

"""
kernel -> linear
training time: 0.096 s
predict time: 0.992 s
predict result ->  [0 1 1 ... 1 0 1]
accuracy ->  0.8845278725824801
"""

"""
kernel -> rbg , unset C
training time: 0.104 s
predict time: 1.062 s
predict result ->  [0 1 1 ... 1 1 1]
accuracy ->  0.6160409556313993
"""

"""
training time C = 10 ---------- 989.043 s
predict time C = 10: ---------- 107.465 s
predict result C = 10 ->  [0 1 1 ... 1 0 1]
accuracy of C = 10 ->  0.810580204778157


training time: ----------  501.474 s
predict time of C = 100 ----------: 50.6 s
predict result of C = 100 ->  [0 0 1 ... 1 0 0]
accuracy of C = 100 ->  0.9550625711035268


training time of C = 1000: ---------- 204.606 s
predict time of C = 1000: ---------- 21.291 s
predict result of C = 1000 ->  [0 0 1 ... 1 0 0]
accuracy of C = 1000 ->  0.9829351535836177


training time of C = 10000: ---------- 112.8 s
predict time of C = 10000: ---------- 10.603 s
predict result of C = 10000 ->  [0 0 1 ... 1 0 0]
accuracy of C = 10000 ->  0.9908987485779295
"""

clf = SVC(kernel="rbf", C=10)
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
t0 = time()
clf.fit(features_train, labels_train)
print "training time C = 10:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "predict time C = 10:", round(time()-t0, 3), "s"

print "predict result C = 10 -> ", pred

print "accuracy of C = 10 -> ", accuracy_score(pred, labels_test)


clf = SVC(kernel="rbf", C=100)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "predict time of C = 100:", round(time()-t0, 3), "s"

print "predict result of C = 100 -> ", pred

print "accuracy of C = 100 -> ", accuracy_score(pred, labels_test)


clf = SVC(kernel="rbf", C=1000)
t0 = time()
clf.fit(features_train, labels_train)
print "training time of C = 1000:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "predict time of C = 1000:", round(time()-t0, 3), "s"

print "predict result of C = 1000 -> ", pred

print "accuracy of C = 1000 -> ", accuracy_score(pred, labels_test)


clf = SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print "training time of C = 10000:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "predict time of C = 10000:", round(time()-t0, 3), "s"

print "predict result of C = 10000 -> ", pred

print "accuracy of C = 10000 -> ", accuracy_score(pred, labels_test)


#########################################################


