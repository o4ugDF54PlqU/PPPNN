
#%%
from numpy import array
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM

#%%
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# load
input_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\"
in_filename = 'elon_full_no_rt.txt'
raw_text = load_doc(input_path+in_filename)
lines = raw_text.split('\n')


#%%
words = []
for line in lines:
	temp_words = line.split()
	for word in temp_words:
		if word not in words:
			words.append(word)

mapping = dict((c, i) for i, c in enumerate(words))
print(mapping)

#%%
sequences = list()
for line in lines:
	# integer encode line
	encoded_seq = [mapping[word] for word in line.split()]
	# store
	sequences.append(encoded_seq)
print(sequences)

#%%
# vocabulary size
vocab_size = len(mapping)
print('Vocabulary Size: %d' % vocab_size)

#%%
sequences = array(sequences)
print(sequences)
X, y = sequences[:,:1], sequences[:,1]

#%%
print(X)
sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
X = array(sequences)
y = to_categorical(y, num_classes=vocab_size)

#%%
# define model
model = Sequential()
model.add(LSTM(900, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.1))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

#%%
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=20, verbose=2)


#%%
# second round of training
in_filename = 'elon_april_to_may.txt'
raw_text = load_doc(input_path+in_filename)
lines = raw_text.split('\n')

sequences = list()
for line in lines:
	# integer encode line
	encoded_seq = [mapping[word] for word in line.split()]
	# store
	sequences.append(encoded_seq)
print(sequences)

sequences = array(sequences)
X, y = sequences[:,:1], sequences[:,1]

sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
X = array(sequences)
y = to_categorical(y, num_classes=vocab_size)

#%%
# fit model
model.fit(X, y, epochs=5, verbose=2)


#%%
# save the model to file
model.save(input_path+'2_stage_proto_model.h5')
# save the mapping
dump(mapping, open(input_path+'2_stage_proto_mapping.pkl', 'wb'))


#%%
