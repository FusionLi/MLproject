#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


	
### your code goes here 

from sklearn.cross_validation import train_test_split
feature_train, feature_test, label_train, label_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()

clf.fit(feature_train, label_train)

prediction = clf.predict(feature_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(prediction, label_test)
print "Accuracy:", accuracy

# Alternative using numpy method
# import numpy as np
# np.count_nonzero(prediction == 1) 
print "POI in prediction:", list(prediction).count(1)#np.count_nonzero(prediction == 1) 

print "Total number of test sets:", len(label_test)

# If your identifier predicted 0. (not POI) for everyone in the test set, its accuracy
print "If your identifier predicted 0. (not POI) for everyone in the test set, its accuracy:", float(label_test.count(0)) / float(len(label_test))

print "Prediction", "Actual"
for predicted, actual in zip(list(prediction), label_test):
	print predicted, actual

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print "Precision score:", precision_score(label_test, prediction)
print "Recall score:", recall_score(label_test, prediction)

