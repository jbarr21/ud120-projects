#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import tree
from sklearn.metrics import accuracy_score

nb_clf = GaussianNB()
dt_clf = tree.DecisionTreeClassifier(min_samples_split=40)
svm_clf = SVC(kernel="rbf", C=10000000000)

clf = AdaBoostClassifier(base_estimator=svm_clf, algorithm='SAMME')
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
labels_pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test, labels_pred)
print 'accuracy = %.2f' % (accuracy * 100)

# 92.4% in 0.104s (max of 95.2% using svm_clf with rfb & C=100000000000)






### visualization code (prettyPicture) to show you the decision boundary
try:
     prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
