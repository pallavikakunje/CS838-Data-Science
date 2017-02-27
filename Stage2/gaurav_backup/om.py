import re

import nltk

#nltk.download()

#features : All Capital[0], more than 2 words[1], strong adjective in the sentence[2], play is in sentence[3], word is noun/not[4], preceeded by by(NO)[5],

feature_list = []

class_list = []

games = []



#find_sentence_regex = r"([^.]*?\<[\+\-][\+\-][\+\-]\> ([a-zA-Z 0-9]+) \<\/[\+\-][\+\-][\+\-]\>[^.]*\.)"

find_sentence_regex = re.compile(r"([^.]*?\<[\+\-][\+\-][\+\-]\> ([a-zA-Z 0-9]+) \<\/[\+\-][\+\-][\+\-]\>[^.]*\.)")

find_games_in_sentence_regex = re.compile(r"\<[\+\-][\+\-][\+\-]\> ([a-zA-Z 0-9]+) \<\/[\+\-][\+\-][\+\-]\>")

capitals_regex = re.compile(r"[A-Z]+[a-z]+")



for files_index in xrange(0,200):

	file_name = "cleaned_data/output_file-"+ str(files_index) + ".txt"

	with open (file_name, "r") as myfile:

	    data=myfile.read()



	sentences = find_sentence_regex.findall(data)



	#### NLTK PART


	#print files_index
	for x in sentences:
		#print files_index
		#print x[0]


		games_in_sentence = find_games_in_sentence_regex.findall(x[0])



		for game in games_in_sentence:



			local_feature_list = [0 for p in range(6)]	



			#all capital 

			match = capitals_regex.search(game)

			if match:

				local_feature_list[0] = 1



			games.append(game)

			

			#play is around the tagged word

			play_word_is_around_regex = re.escape(game) + r"\W+(?:\w+\W+){1,6}?play|play\W+(?:\w+\W+){1,6}?" + re.escape(game)

			match = re.search(play_word_is_around_regex, x[0])

			if match:

				local_feature_list[3] = 1



			# noun feature

			text = nltk.word_tokenize(unicode(x[0], 'utf-8'))

			tags = nltk.pos_tag(text)

			#print tags

			name_tokenized = game.split()

			#more than 2 words

			if len(name_tokenized) > 2:

				local_feature_list[1] = 1

			tag_for_name = [i for i in tags if i[0] == name_tokenized[0]]

			#print tag_for_name



			if tag_for_name and tag_for_name[0][1] == 'NNP':

				local_feature_list[4] = 1



			# strong adjective

			for i in tags:

				if i[1] == 'JJ' or i[1] =='JJR' or i[1] == 'JJS':

					local_feature_list[2] = 1

			



			#preceded by by

			sentence_tokenized = x[0].split()

			#print sentence_tokenized

			index_of_game = sentence_tokenized.index(name_tokenized[0])

			if index_of_game - 2 >= 0:

				if sentence_tokenized[index_of_game - 2] == "by":

					local_feature_list[5] = 1



			#print local_feature_list



			if sentence_tokenized[index_of_game - 1] == "<+++>":

				class_list.append(1)

			else :

				class_list.append(0)



			feature_list.append(local_feature_list)



f = open ('feature_list/feature_list','w')
f.write(str(feature_list))
f.close()

f = open ('class_list/class_list','w')
f.write(str(class_list))
f.close()

print feature_list

print class_list

print games
