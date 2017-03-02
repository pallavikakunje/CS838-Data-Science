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

#feature set and class of tags in first 200 documents to learn the model using SVM
#as SVM was the best classifier obtained in the cross validation step.
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

#print "============= check predict & actual=============="
print "***OUTPUT***"

#learning SVM model here.
model = svm.SVC()
model.fit(feature_list, class_list)

#feature set and class of tags in the last 100 documents to predict using SVM.
f = open('test_list/feature_list','r')
data = f.read()
test_list = []
i = 1
while(i<len(data)-1):
    if(data[i] == '['):
        temp=[]
        while(data[i]!=']'):
            if(data[i]=='0' or data[i]=='1'):
                temp.append(int(data[i]))
            i+=1
        test_list.append(temp)
    i+=1
f.close()
f = open('test_list/class_list','r')
data = f.read()
actual_list = []
for i in data:
    if(i=='0' or i=='1'):
        actual_list.append(int(i))
f.close()

#counting predicted and actual class 
i = 0
TP=0.0
TN=0.0
FP=0.0
FN=0.0
for temp in test_list:
	temp = np.array(temp).reshape((1, -1))
	if(model.predict(temp) == actual_list[i]):
		if(actual_list[i] == 1):
			TP+=1
		elif(actual_list[i] == 0):
			TN+=1
	else:
		if(actual_list[i] == 1):
			FN+=1
		elif(actual_list[i] == 0):
			FP+=1
	i += 1

#calculating and printing precision and recall
print "precision:", TP/(TP+FP), "recall:", TP/(TP+FN)

#print "**********************end*************************"

