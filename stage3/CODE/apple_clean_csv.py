import re

#open .json file to read the data and .csv file to write the data.
fp = open("apple.json","r")
qp = open("apple.csv","w")

#file line in the file for providing headings.
a = '"ID",'+'"name",'+'"category",'+'"developer",'+'"rating"'
qp.write(a)
qp.write('\n')

#initializing j here which will act as ID.
j = 0

#reading each line of the file and extracting the required information.
for line in fp:
	#writing ID in the first field
	j = j + 1
	a = '"b'+str(j)+'",'
	qp.write(a)
	word = line.split()

	#extracting game name here
	for i in range(0,len(word)):
		if (word[i] == '"title":'):
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
		if (word[i] == '"meta":'):
			while(word[i] != 'Games,'):
				i = i + 1
			a = '"'
			i = i + 1
			regex = r'.*\,$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			a = a.replace(',','')
			a = a + '",'
			qp.write(a)
			break

	#extracting developer name here
	for i in range(0,len(word)):
		if (word[i] == '"devloper":'):
			a = ""
			i = i + 1
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			#print a
			qp.write(a[:1]+a[4:])
			break

	#extracting game's rating
	for i in range(0,len(word)):
		if (word[i] == '"current_version_rating":'):
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
