import re
import sys

"""
#this function removes comma and full stops
def clean_word(data):
	i = 0;
	while(i<len(data)):
		if(data[i] == '.' or data[i]==','):
			data[i]. = " "
		i = i + 1
"""

def main():
	stop_words = ['The','A','This', 'And', 'So', 'There', 'But', 'If', 'Not', 'It', 'You', 'Your', 'TouchArcade', 'YouTube', 'Subscribe', 'While']
	with open ('cleaned_data/'+sys.argv[1], "r") as myfile:
		data = myfile.read()
	#clean_word(data)
	#words = data.split()
	data = data.replace('.','. ')
	words = data.split()

	#regex = r"([a-zA-Z]+)"
 	#for 1st letter capital followed by anything
	#regex = r"[A-Z][a-z][A-Za-z]*$"
	#for all letters capital
	#regex = r"^[A-Z]*$"

	counter_pos = 0
	counter_neg = 0

	f = open ('cleaned_data/output_'+sys.argv[1],'w')
		
	regex = r"[A-Z][a-z][A-Za-z]*$"
	i = 0;
	prev_neg = 0
	while(i < len(words)):
		neg_word = 0
		match = re.search(regex, words[i])
		if (match):
			if(words[i-1]=='<+++>'):
				counter_pos = counter_pos + 1
				while(words[i]!='</+++>'):
					#write to file
					f.write(words[i])
					f.write(' ')
					i = i + 1
					if (i >= len(words)):
						f.close()
						print "positive:", counter_pos, "negetive:", counter_neg
						sys.exit()
			else:
				j = 0
				while(j < len(stop_words)):
					if(words[i] == stop_words[j]):
						break
					else:
						j = j + 1
				if(j == len(stop_words)):
					#mark this as negetive example. Add <---> at start and </---> at the end
					#print match.group(0)
					neg_word = 1
					#print words[i+1]

		if(neg_word == 1 and prev_neg == 0):
			f.write('<---> ')
			counter_neg = counter_neg + 1
			f.write(words[i])
			f.write(' ')
			prev_neg = 1
		elif(neg_word == 1 and prev_neg == 1):
			f.write(words[i])
			f.write(' ')
		elif(neg_word == 0 and prev_neg == 1):
			f.write('</---> ')
			f.write(words[i])
			f.write(' ')
			prev_neg = 0
		else:
			f.write(words[i])
			f.write(' ')
		i = i + 1

	#print "positive:", counter_pos, "negetive:", counter_neg
	f.close()

if __name__ == '__main__':
	main()






