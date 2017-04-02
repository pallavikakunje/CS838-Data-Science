import re

fp = open("playstore.txt","r")
qp = open("appstore.txt","r")

count = 0
for linep in fp:
	#print linep
	qp = open("appstore.txt","r")
	for lineq in qp:
		#print lineq
		if(linep == lineq):
			#print linep
			count = count + 1
	qp.close()	

print count
