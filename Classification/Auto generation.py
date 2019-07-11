#%%
from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

#%%
input_path = 'C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\'
# load the model
model = load_model(input_path+'multi_user_WL5_model.h5')
# load the mapping
mapping = load(open(input_path+'multi_user_WL5_mapping.pkl', 'rb'))

#%%
# generate a sequence of characters with a language model
def generate_seq(model, mapping, seq_length, seed_text, n_chars):
	in_text = seed_text
	# generate a fixed number of characters
	for _ in range(n_chars):
		# encode the characters as integers
		encoded = [mapping[0][word] for word in in_text.split()]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# one hot encode
		encoded = to_categorical(encoded, num_classes=len(mapping[0]))
		print(encoded)
		encoded = encoded.reshape(1, encoded.shape[1], encoded.shape[2])
		# predict character
		yhat = model.predict_classes(encoded, verbose=0)
		# reverse map integer to character
		out = ''
		for word, index in mapping[1].items():
			if index == yhat:
				out = str(word)
				break
		# append to input
		in_text = in_text+ " " + out
	return in_text
 
#%%
generate_seq(model, mapping, 5, "they get their shit straight", 1)

#%%
