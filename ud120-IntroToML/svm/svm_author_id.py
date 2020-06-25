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
from sklearn.svm import SVC

clf=SVC(kernel='rbf',C=10000)

#slicing dataset to increase speed
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

t0=time()
clf.fit(features_train,labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1=time()
predictions=clf.predict(features_test)
print ("prediction time:", round(time()-t1, 3), "s")

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(labels_test,predictions)
print(accuracy)
## get number of times model predicted chris
count=0
for p in predictions:
    if p==1:
        count+=1
print(count)
#########################################################


