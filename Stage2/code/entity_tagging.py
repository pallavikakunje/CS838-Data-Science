import re
import sys

def main():
	#reading data from the file
	with open ('cleaned_data/'+sys.argv[1], "r") as myfile:
		data = myfile.read()

	#cleaning data so that words are separated clearly.
	data = data.replace('.','. ')
	data = data.replace('  ',' ')
	data = data.replace(',','')
	data = data.replace('</+++>/<+++>', '</+++> <+++>')
	data = data.replace('</+++><+++>', '</+++> <+++>')
	data = data.replace("'s",'')
	data = data.replace("\"",'')
	
	#saving all the words as a list.
	words = data.split()

	f = open ('cleaned_data/output_'+sys.argv[1],'w')
	
	regex = r"[A-Z][a-z]*$"
	i = 0
	count = 0

	#marking tags in the first 300 words of the file. Limiting the count as 300 as files are very large
	#we are getting enough tags in the first 300 words.
	while(i < min(len(words),300)):
		idx = words[i].find('<+++>')
		if(idx != -1):
			if(idx != 0):
				words[i] = words[i][:idx]+" "+words[i][idx:]
				
			while(words[i].find('</+++>') == -1):
				f.write(words[i])
				f.write(' ')
				i+=1

		elif(re.search(regex, words[i])):
				count = (count + 1)%2
				temp = ""
				flag = 0
				while(re.search(regex, words[i])):
					temp+=words[i]+" "
					if(words[i].isupper()):
						flag = 1
					i+=1
					if(i >= len(words)):
						break
				if(flag == 0 and count == 1):
					f.write('<---> ')
					f.write(temp)
					f.write('</---> ')
				else:
					f.write(temp)
			
		else:
			f.write(words[i])
			f.write(' ')
			i+=1
	f.write('.')
	f.close()
	
if __name__ == '__main__':
	main()
