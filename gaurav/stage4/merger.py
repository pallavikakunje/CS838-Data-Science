import re

#all_predictions.csv is contains predicted output for all potential matches.
#In this script, we are checking for each potential match whether it is
#predicted as match or not. It it is matched then we are copying both tuples
#in matched_tuples.csv. We are merging both tuples according to merger rules
#and copying the merged tuple in merged_tuples.csv.
fq = open('all_predictions.csv','r')
fp = open('merged_tuples.csv','w')
ft = open('matched_tuples.csv','w')

#first line in merged_tuples.csv file for providing headings.
a = '"ID",'+'"name",'+'"category",'+'"developer",'+'"rating"'
fp.write(a)
fp.write('\n')

#first line in matched_tuples.csv file for providing headings.
#Each line in this file contains matched tuples from both google table and apple table.
a = '"G_ID",'+'"G_name",'+'"G_category",'+'"G_developer",'+'"G_rating",'+'"A_ID",'+'"A_name",'+'"A_category",'+'"A_developer",'+'"A_rating"'
ft.write(a)
ft.write('\n')

#initializing j here which will act as ID.
j = 0

for line in fq:
	word = line.split()
	#checking if the rows are predicted as matched or not.
	if(word[len(word)-1] == "1"):
		#writing ID in the first field
		j = j + 1
		idx = '"'+str(j)+'",'
		fp.write(idx)

		#extracting row number of each tuple which are being matched.
		word_google = word[2]
		word_apple = word[3]

		#variables to hold attribute values of google table
		ID_google = ""
		name_google = ""
		category_google = ""
		developer_google = ""
		rating_google = ""

		#variables to hold attribute values of apple table
		ID_apple = ""
		name_apple = ""
		category_apple = ""
		developer_apple = ""
		rating_apple = ""
		
		with open('google.csv') as fr:
			with open('apple.csv') as fs:
				#based on the extracted row number, reading the corresponding row from google table
				#and writing whole row in matched_tuples.csv file.
				content_google = fr.read().splitlines()
				row = content_google[int(word_google[1:-1])]
				ft.write(row)
				ft.write(",")

				#extracting different attribute values for merging.
				#extracting ID.
				start = row.find('"') + 1
				end = row.find('"', start)
				ID_google = row[start:end]

				#extracting name.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				name_google = row[start:end]
				
				#extracting category.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				category_google = row[start:end]

				#extracting developer.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				developer_google = row[start:end]

				#extracting rating.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				rating_google = row[start:end]

				#based on the extracted row number, reading the corresponding row from apple table
				#and writing whole row in matched_tuples.csv file.
				content_apple = fs.read().splitlines()
				row = content_apple[int(word_apple[1:-1])]
				ft.write(row)
				ft.write('\n')
				
				#extracting different attribute values for merging.
				#extracting ID.
				start = row.find('"') + 1
				end = row.find('"', start)
				ID_apple = row[start:end]
				
				#extracting name.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				name_apple = row[start:end]
				
				#extracting category.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				category_apple = row[start:end]

				#extracting developer.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				developer_apple = row[start:end]
				
				#extracting rating.
				row = row[(end+1):]
				start = row.find('"') + 1
				end = row.find('"', start)
				rating_apple = row[start:end]
				
				#if both google table and apple table contain rating then taking average of both ratings.
				#Otherwise, taking rating from google table.
				if((rating_apple.find('Ratings') == -1) and (rating_apple.find('none') == -1)):
					rating_google = (float(rating_google) + float(rating_apple))/2

				#combining all attributes as a single string and writing it in the file merged_tuples.csv.
				to_write = '"'+name_google+'",'+'"'+category_google+'",'+'"'+developer_google+'",'+'"'+str(rating_google)+'"'
				fp.write(to_write)
				fp.write('\n')

fp.close()
fq.close()
ft.close()







































