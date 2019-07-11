
#%%
from numpy import array
import numpy as np
from pickle import dump
from pickle import load
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM

#%%
# load
input_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\"
in_filename = 'multi_user_WL5.txt'
with open(input_path+in_filename, 'rb') as pickle_file:
    sequences = load(pickle_file)
len(sequences)

#%%
import random
random.shuffle(sequences)

#%%
userids = []
words = []
count = 0
for line in sequences:
	count+=1
	text = line[1]
	if count % 10000 == 0:
		print(count)
	for word in text:
		if word not in words:
			words.append(word)
	if line[0] not in userids:
		userids.append(line[0])

mapping = dict((c, i) for i, c in enumerate(words))
print(mapping)
id_mapping = dict((c, i) for i, c in enumerate(userids))
print(id_mapping)

#%%
encoded = list()
for line in sequences:
	# integer encode line
	encoded_seq = []
	for word in line[1]:
		encoded_seq.append(mapping[word])
	# store
	encoded.append(encoded_seq)

X = np.array(encoded)

#%%
encoded = list()
for line in sequences:
	# integer encode line
	encoded_seq = [id_mapping[line[0]]]
	# store
	encoded.append(encoded_seq)
y = np.array(encoded)

#%%
# vocabulary size
vocab_size = len(mapping)
id_size = len(id_mapping)
print('Vocabulary Size: %d' % vocab_size)
print('ID size: %d' % id_size)

#%%
# one hot
del sequences
X = array([to_categorical(x, num_classes=vocab_size) for x in X])
y = to_categorical(y, num_classes=id_size)

#%%
# define model
model = Sequential()
model.add(LSTM(700, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.1))
model.add(Dense(id_size, activation='softmax'))
print(model.summary())

#%%
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=10, verbose=1)

#%%
# save the model to file
model.save(input_path+'multi_user_WL5_model.h5')
# save the mapping
dump([mapping, id_mapping], open(input_path+'multi_user_WL5_mapping.pkl', 'wb'))


#%%


#%%
