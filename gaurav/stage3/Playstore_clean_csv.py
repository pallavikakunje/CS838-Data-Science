import re
from unidecode import unidecode

fp = open("playstore.json","r")
qp = open("playstore_formatted.csv","w")

#fp = open("test.json","r")
#qp = open("gaurav.txt","w")
j = 0
a = '"a'+str(j)+'",'+'"name",'+'"category",'+'"developer",'+'"rating"'
qp.write(a)
qp.write('\n')
for line in fp:
	j = j + 1
	a = '"a'+str(j)+'",'
	qp.write(a)
	word = line.split()
	for i in range(0,len(word)):
		if (word[i] == '"app_name":'):
			a = ""
			i = i + 1
			#while(word[i][len(word[i])-2]!='"'):
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):	
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			#print a,
			qp.write(a)
			break

	for i in range(0,len(word)):
		if (word[i] == '"genre":'):
			a = ""
			i = i + 1
			#while(word[i][len(word[i])-2]!='"'):
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			#print a,
			qp.write(a)
			break

	for i in range(0,len(word)):
		if (word[i] == '"developer":'):
			a = ""
			i = i + 1
			#while(word[i][len(word[i])-3]!='"'):
			while(word[i].find('}')==-1):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			a = a.replace('}','')
			#print a
			qp.write(a)
			break

	for i in range(0,len(word)):
		if (word[i] == '{"rating":'):
			a = ""
			i = i + 1
			#while(word[i][len(word[i])-2]!='"'):
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			word[i] = word[i].replace(',','')
			a = a + word[i]
			#print a,
			qp.write(a)
			break

	qp.write('\n')

fp.close()
qp.close()
"""
for word in line.split():
	if (word == '{"rating":'):
 		print word
"""
"""
for line in fp:
        for word in line.split():
	   if(word == '"description":'):
	   	print(word) 
"""
