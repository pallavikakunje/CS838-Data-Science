import re

fp = open("appstore.json","r")
qp = open("appstore_formatted.csv","w")

#fp = open("test.json","r")
#qp = open("appstore_formatted.csv","w")
j = 0
a = '"ID",'+'"name",'+'"category",'+'"developer",'+'"rating"'
qp.write(a)
qp.write('\n')
for line in fp:
	j = j + 1
	a = '"b'+str(j)+'",'
	qp.write(a)
	word = line.split()
	for i in range(0,len(word)):
		if (word[i] == '"title":'):
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
		if (word[i] == '"meta":'):
			while(word[i] != 'Games,'):
				i = i + 1
			a = '"'
			i = i + 1
			#while(word[i][len(word[i])-2]!='"'):
			regex = r'.*\,$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			a = a.replace(',','')
			a = a + '",'
			#print a,
			qp.write(a)
			break

	for i in range(0,len(word)):
		if (word[i] == '"devloper":'):
			a = ""
			i = i + 1
			#while(word[i][len(word[i])-3]!='"'):
			regex = r'.*\",$'
			while(not re.search(regex, word[i])):
				a = a + word[i] + " "
				i = i + 1
			a = a + word[i]
			#print a
			qp.write(a[:1]+a[4:])
			break

	for i in range(0,len(word)):
		if (word[i] == '"current_version_rating":'):
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
