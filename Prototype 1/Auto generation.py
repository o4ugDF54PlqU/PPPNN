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
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
import csv
import nltk
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
path = get_tmpfile("word2vec.model")
modelw2v = Word2Vec(min_count=1, workers=6)
modelw2v.save("word2vec.model")
from nltk.corpus import stopwords
stops_words = set(stopwords.words('english'))

usage_dict = {}
sentences = []
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
			sentences.append(" ".join(temp))
			for word in temp:
				if word not in usage_dict:
					usage_dict[word] = 1
				else:
					usage_dict[word] += 1
			line_count+=1
	print(f'Processed {line_count} lines.')

#removing stopwords
nouns_in_tweet = []
for item in usage_dict:
	if item in nouns and item not in stops_words:
		nouns_in_tweet.append(item)



#%%
# Trains the word2vec model
split_sent = []
for sentence in sentences:
	split_sent.append(sentence.split())

modelw2v.build_vocab(split_sent)
modelw2v.train(split_sent, total_examples=len(sentences), epochs=100)

#%%
# Each noun is given a score based on how often a related word is used
# multiplied by how related (0-1) that word is, for the top 10 most related
scores = dict()
for noun in nouns_in_tweet:

	scores[noun] = usage_dict[noun]
	relations = modelw2v.most_similar(positive=[noun], topn = 10)
	for rel in relations:
		scores[noun] += usage_dict[rel[0]] * rel[1]

#%%
# Generates using the top scoring word as the starter
count = 0
sorted_list = sorted(scores, key = scores.__getitem__)
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
