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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
labels_pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test, labels_pred)
print 'accuracy = %.2f' % (accuracy * 100)

# with linear on 100% of data: 98.4% in 148s
# with linear on 1% of data: 88.5% in 0.083s
# with rbf & C=1 on 1% of data: 61.6% in 0.083s
# with rbf & C=10 on 1% of data: 61.6% in 0.084s
# with rbf & C=100 on 1% of data: 61.6% in 0.088s
# with rbf & C=1000 on 1% of data: 82.1% in 0.09s
# with rbf & C=10000 on 1% of data: 89.3% in 0.083s
# with rbf & C=10000 on 100% of data: 99.1% in 98.573s

# returns [1 0 1]
print clf.predict(features_test[[10, 26, 50]])

print 'num items that are [1] = %d' % len([pred for pred in labels_pred if pred == 1])
#########################################################


