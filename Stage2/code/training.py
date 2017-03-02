import re
from nltk.corpus import wordnet
import nltk
import operator
from stop_words import get_stop_words

# define stop words
stop_words = get_stop_words('english')
stop_words.append('TouchArcade')
stop_words.append('YouTube')
stop_words.append('Subscribe')
stop_words.append('iOS')
stop_words.append('iPad')
stop_words.append('iPhone')
stop_words.append('Apple')
stop_words.append('iCloud')


def any_common_word(str1, str2):
	str1 = str1.split()
	str2 = str2.split()
	for w in str1:
		if w in str2:
			return True
	else:
		return False


## Global Variables 

#New features : preceeded by by(NO)[0], stop_words[1], count feature[2], has_stop_words_other_than[3], contains_$[4], no_word_in_dict[5]"
feature_list = []
class_list = []
games = []
global_game_counter = 0
features_num = 6

# Regular expressions 
find_sentence_regex = re.compile(r"([^.]*?\<[\+\-][\+\-][\+\-]\> ([a-zA-Z 0-9:!\-\'&]+) \<\/[\+\-][\+\-][\+\-]\>[^.]*\.)")
find_games_in_sentence_regex = re.compile(r"\<[\+\-][\+\-][\+\-]\> ([a-zA-Z 0-9:!\-\'&]+) \<\/[\+\-][\+\-][\+\-]\>")
capitals_regex = re.compile(r"[A-Z]+[a-z]+")


features_file_path = "test_list/feature_list"
class_file_path = "test_list/class_list"


for files_index in xrange(0,200):

	file_name = "cleaned_data/output_file-"+ str(files_index) + ".txt"

	# open file for extracting data
	with open (file_name, "r") as myfile:
	    data = myfile.read()

	# collect all the sentences which has tags
	sentences = find_sentence_regex.findall(data)

	games_count = {}
	games_in_current_file = []
	game_start_index_current_file = global_game_counter
	for x in sentences:
		games_in_sentence = find_games_in_sentence_regex.findall(x[0])
		#print x
		remove_list = ['<--->', '</--->', '<+++>', '</+++>']
		word_list = x[0].split()
		#print word_list
		sentence = ' '.join([i for i in word_list if i not in remove_list])

		for game in games_in_sentence:
			local_feature_list = [0 for p in range(features_num)]
			games.append(game)
			games_in_current_file.append(game)
			global_game_counter += 1
			
			# iterate over games_count dict and fill if not present otherwise increment the count
			key_list = list(games_count)
			found = 0
			for key in key_list:
				if game in key:
					found = 1
					if game.lower() not in stop_words:
						games_count[key] += 1
						break
			if found == 0:
				games_count[game] = 1

			name_tokenized = game.split()
			
			spl = game.split()

			# Check if $ in price after game name
			if(word_list.index(spl[len(spl)-1]) < len(word_list) -2):
				check_price = word_list[word_list.index(spl[len(spl)-1]) + 2]
				if('$' in check_price):
					#print check_price
					local_feature_list[4] = 1
			tag_for_name = [i for i in tags if i[0] == name_tokenized[0]]

			text_len = len(text)

			# See if it is preceeded by some famous words
			sentence_tokenized = sentence.split()
			#print sentence_tokenized
			index_of_game = sentence_tokenized.index(name_tokenized[0])
			if index_of_game - 1 >= 0:
				if sentence_tokenized[index_of_game - 1] == "by" or  sentence_tokenized[index_of_game - 1] == "from" or sentence_tokenized[index_of_game - 1] == "developer":
					local_feature_list[0] = 1


			# stop word feature 
			if len(name_tokenized) == 1:
				if name_tokenized[0].lower() in stop_words:
					local_feature_list[1] = 1


			# if at the begining of the sentence and length is one
			if len(name_tokenized) == 1:
				if sentence.index(game) == 0:
						local_feature_list[2] = 1


			# Declare class of the game tag
			original_sentence_tokenized = x[0].split()
			index_of_game = original_sentence_tokenized.index(name_tokenized[0])
			if original_sentence_tokenized[index_of_game - 1] == "<+++>":
				class_list.append(1)
			else :
				class_list.append(0)
			feature_list.append(local_feature_list)
			
			# Check if all words are not in English Language and if stop words are in game
			flag_gm = 0
			for i in name_tokenized:
				if ((i in stop_words) and (i != 'of') and (i != 'the') and (i != 'and')):
					flag_gm = 1
			if(flag_gm == 1 and len(name_tokenized)>1):
				local_feature_list[3] = 1
			flag_gm = 0
			for i in name_tokenized:
				if wordnet.synsets(i.lower()):
					flag_gm = 1

			if(flag_gm == 0 and len(name_tokenized)>1):
				local_feature_list[5] = 1

	sorted_games_count = sorted(games_count.items(), key=operator.itemgetter(1))
	sorted_games_count.reverse()
	GAME_NAME = sorted_games_count[0][0]

	# Count feature - find the number of occurances of the word and take a call to include it or not 
	for game, index in zip(games_in_current_file, range(0, len(games_in_current_file))):
		if feature_list[game_start_index_current_file + index][2] == 1:
			# single and start of the sentence
			if game in GAME_NAME:
				feature_list[game_start_index_current_file + index][2] = 0
		else :
			# not at the start of sentence
			if any_common_word(game, GAME_NAME) == True:
				#print "in else true "
				feature_list[game_start_index_current_file + index][2] = 0
			else:
				split_game = game.split()
				if len(split_game) > 1:
					# multiword
					feature_list[game_start_index_current_file + index][2] = 0
				else:
					feature_list[game_start_index_current_file + index][2] = 1


# writing to files all features and clas
f = open (features_file_path,'w')
f.write(str(feature_list))
f.close()
f = open (class_file_path,'w')
f.write(str(class_list))
f.close()
