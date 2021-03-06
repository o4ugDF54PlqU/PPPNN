#%%
from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

#%%
input_path = 'C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\'
# load the model
model = load_model(input_path+'model_WL1.h5')

#%%
# load the mapping
mapping = load(open(input_path+'mapping_WL1.pkl', 'rb'))

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
		encoded = encoded.reshape(1, encoded.shape[1], encoded.shape[2])
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
# test
print(generate_seq(model, mapping, 2, 'got mars', 20))
# test
print(generate_seq(model, mapping, 2, 'spend some', 20))
# test
print(generate_seq(model, mapping, 2, 'solar power', 20))
#%%
