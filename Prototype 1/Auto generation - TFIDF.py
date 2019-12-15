#%%
from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

#%%
input_path = 'C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\'
# load the model
model = load_model(input_path+'2_stage_proto_model.h5')
# load the mapping
mapping = load(open(input_path+'2_stage_proto_mapping.pkl', 'rb'))

#%%
# generate a sequence of characters with a language model
def generate_seq(model, mapping, seq_length, seed_text, n_chars):
	in_text = seed_text
	# generate a fixed number of characters
	for _ in range(n_chars):
		# encode the characters as integers
		encoded = [mapping[word] for word in in_text.split()]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# one hot encode
		encoded = to_categorical(encoded, num_classes=len(mapping))
		encoded = encoded.reshape(1, encoded.shape[0], encoded.shape[1])
		# predict character
		yhat = model.predict_classes(encoded, verbose=0)
		# reverse map integer to character
		out = ''
		for word, index in mapping.items():
			if index == yhat:
				out = word
				break
		# append to input
		in_text = in_text+ " " + out
	return in_text
 



#%%
# Loading NLTK
import csv
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
stops_words = set(stopwords.words('english'))

sentences = []
used_words = []
with open('C:\\Users\\iD Student\\Documents\\PPNN\\Raw data\\elonmusk_tweets.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count+=1
		elif "RT " in row[2]:
			line_count+=1
		else:
			temp = row[2][2:-1].split()
			for word in temp:
				if '/' in word:
					temp.remove(word)
				elif '\\' in word:
					temp.remove(word)
				elif '@' in word:
					temp.remove(word)
			for word in temp:
				if word not in used_words:
					used_words.append(word)
			sentences.append(temp)
			line_count+=1
	print(f'Processed {line_count} lines.')

#%%
new_sentences = []
count = 0
temp = []
for tweet in sentences:
	for word in tweet:
		temp.append(word)
	count += 1
	if count % 25 == 0 or count == len(sentences):
		new_sentences.append(temp)
		temp = []
sentences = new_sentences[:]

#%%
# Calculates TF
dicts = []
for tweet in sentences:
	tweet_dict = {}
	count = 0
	for word in tweet:
		count += 1
		try:
			tweet_dict[word] += 1
		except KeyError:
			tweet_dict[word] = 1
	for word in tweet_dict:
		tweet_dict[word] /= count
	dicts.append(tweet_dict)


#%%
# Calculate IDF
import math
IDF = {}
for used_word in used_words:
	IDF[used_word] = 0
	for tweet in sentences:
		for word in tweet:
			if used_word == word:
				IDF[used_word] += 1
				break
	IDF[used_word] = math.log10(len(sentences)/IDF[used_word])

#%%
# calculates TFIDF
TFIDF = {}
word_count = {}
for word in dicts[3]:
	if word not in TFIDF:
		TFIDF[word] = dicts[3][word] * IDF[word]
		word_count[word] = 1
	else:
		TFIDF[word] += dicts[3][word] * IDF[word]
		word_count[word] += 1

#%%
TFIDF

#%%
# Generates based on TFIDF order
count = 0
sorted_list = sorted(TFIDF, key = TFIDF.__getitem__)
for word in sorted_list[::-1]:
	final_pass = []
	count2 = 0
	gen_words = generate_seq(model, mapping, 1, word, 5).split()
	for gword in gen_words:
		if gword not in stops_words:
			final_pass.append(gword)
			count2+=1
		if count2 == 3:
			break
	final_pass = "".join(final_pass)
	print(final_pass)
	count+=1
	if count == 10:
		break

#%%
