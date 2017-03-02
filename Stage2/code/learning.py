# -*- coding: utf-8 -*-
import  sys
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import StratifiedKFold
import sklearn as sk
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
import operator
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

#print "=========== read feature list & class list==================="
f = open('class_list/class_list','r')
data = f.read()
class_list = []
for i in data:
    if(i=='0' or i=='1'):
        class_list.append(int(i))
f.close()

f = open('feature_list/feature_list','r')
data = f.read()
feature_list = []
i = 1
while(i<len(data)-1):
    if(data[i] == '['):
        temp=[]
        while(data[i]!=']'):
            if(data[i]=='0' or data[i]=='1'):
                temp.append(int(data[i]))
            i+=1
        feature_list.append(temp)
    i+=1
f.close()

# print "=========== CV scores from Classifiers ========="
scores = {}
classifiers = {'DecisionTree' : DecisionTreeClassifier(random_state=0), 'SVM' : svm.SVC(probability=True, random_state=0), 'RandomForest' :
	RandomForestClassifier(), 'kNN' :KNeighborsClassifier(5), 'LogisticRegression': LogisticRegression()}
for c in classifiers:
	precision = cross_val_score(classifiers[c], feature_list, class_list, cv=5, scoring='precision')
	recall = cross_val_score(classifiers[c], feature_list, class_list, cv=5, scoring='recall')
	scores[c] = [ precision.mean(), recall.mean()]

print scores

#print "================ Linear Regression CV =============="
skf = StratifiedKFold(n_splits=5)
i = 0
for train_index, test_index in skf.split(feature_list, class_list):
	X_train = []
	y_train = []
	X_test = []
	y_test = []
	for t in train_index:
		X_train.append(feature_list[t])
         	y_train.append(class_list[t])
	for t in test_index:
		X_test.append(feature_list[t])
         	y_test.append(class_list[t])

	model = LinearRegression()
	model.fit(X_train, y_train)
	predicted = []

	for test in X_test:
		test = np.array(test).reshape((1, -1))
		p = model.predict(test)
		if p >= 0.5:
			predicted.append(1)
		else:
			predicted.append(0)
	actual = y_test
	Precision = Recall = 0.0
	tp = fp = tn = fn = 0.0
	for i in range(len(actual)):
		if(actual[i] == 1):
			if(predicted[i] == 1):
				tp += 1
			else:
				fn += 1
		else:
			if(predicted[i] == 0):
				tn += 1
			else:
				fp += 1
	#print "TP: "+str(tp)
	#print "FP: "+str(fp)
	#print "TN: "+str(tn)
	#print "FN: "+str(fn)
	P = (tp / (tp+fp))*100
	R = (tp / (tp+fn))*100
	if(P > Precision):
		Precision = P
		Recall = R
print "LinearRegression P: " + str(Precision)
print "LinearRegression R: " + str(Recall)
#print "**************end***************"
