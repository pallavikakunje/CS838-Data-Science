import re
from unidecode import unidecode

#open .json file to read the data and .csv file to write the data.
fp = open("google.json","r")
qp = open("google.csv","w")

#file line in the file for providing headings.
a = '"ID",'+'"name",'+'"category",'+'"developer",'+'"rating"'
qp.write(a)
qp.write('\n')

#initializing j here which will act as ID.
j = 0

for line in fp:
	#writing ID in the first field
	j = j + 1
	a = '"a'+str(j)+'",'
	qp.write(a)
	word = line.split()

	#extracting game name here
	for i in range(0,len(word)):
		if (word[i] == '"app_name":'):
			a = ""
			i = i + 1
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):	
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			qp.write(a)
			break

	#extracting game's category here
	for i in range(0,len(word)):
		if (word[i] == '"genre":'):
			a = ""
			i = i + 1
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			qp.write(a)
			break

	#extracting developer name here
	for i in range(0,len(word)):
		if (word[i] == '"developer":'):
			a = ""
			i = i + 1
			while(word[i].find('}')==-1):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			a = a.replace('}','')
			qp.write(a)
			break

	#extracting game's rating
	for i in range(0,len(word)):
		if (word[i] == '{"rating":'):
			a = ""
			i = i + 1
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			word[i] = word[i].replace(',','')
			a = a + word[i]
			qp.write(a)
			break

	#moving to next line
	qp.write('\n')

fp.close()
qp.close()
