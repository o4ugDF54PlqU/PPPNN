
#%%
from numpy import array
import numpy as np
from pickle import dump
from pickle import load
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.preprocessing.sequence import pad_sequences

#%%
# load
input_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\"
in_filename = 'multi_user_WL5.txt'
with open(input_path+in_filename, 'rb') as pickle_file:
    sentences = load(pickle_file)


#%%
import random
random.shuffle(sentences)

#%%
fold1 = []
fold2 = []
fold3 = []
for i in range(len(sentences)):
	if i < 15000:
		fold1.append(sentences[i])
	elif i < 30000:
		fold2.append(sentences[i])
	elif i < 45000:
		fold3.append(sentences[i])

#%%
userids = []
words = []
count = 0
for line in sentences:
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
def encode_text(fold, mapping):
	encoded = list()
	encoded_id = list()
	for line in fold:
		# integer encode line
		encoded_seq = []
		for word in line[1]:
			encoded_seq.append(mapping[word])
		# store
		encoded.append(encoded_seq)
		encoded_id.append([id_mapping[line[0]]])

	return array(encoded),array(encoded_id)

X1, Y1 = encode_text(fold1+fold2, mapping)
X2, Y2 = encode_text(fold2+fold3, mapping)
X3, Y3 = encode_text(fold3+fold1, mapping)
print(X1, Y1)
#%%
# vocabulary size
vocab_size = len(mapping)
id_size = len(id_mapping)
print('Vocabulary Size: %d' % vocab_size)
print('ID size: %d' % id_size)

#%%
# one hot
X = array([to_categorical(x, num_classes=vocab_size) for x in X1])
y = to_categorical(Y1, num_classes=id_size)

#%%
# define model
model = Sequential()
model.add(Dense(700, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(id_size, activation='softmax'))
print(model.summary())

#%%
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=10, verbose=1)

#%%
def generate_seq(model, mapping, seq_length, seed_text, n_chars):
	# encode the characters as integers
	encoded = [mapping[word] for word in seed_text]
	# truncate sequences to a fixed length
	encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
	# one hot encode
	encoded = to_categorical(encoded, num_classes=len(mapping))
	encoded = encoded.reshape(1, encoded.shape[1], encoded.shape[2])
	# predict character
	out = model.predict_classes(encoded, verbose=0)
	for word, index in id_mapping.items():
		if out == index:
			return word

#%%
def compare_with_test(test):
	correct = 0
	for line in test:
		if generate_seq(model, mapping, 5, line[1], 1) == line[0]:
			correct += 1
	acc = correct/30000
	print(acc)
	return acc

acc1 = compare_with_test(fold3)
#%%
# one hot
X = array([to_categorical(x, num_classes=vocab_size) for x in X2])
y = to_categorical(Y2, num_classes=id_size)

# define model
del model
model = Sequential()
model.add(Dense(700, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(id_size, activation='softmax'))
print(model.summary())

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=10, verbose=1)

acc2 = compare_with_test(fold1)
#%%
# one hot
X = array([to_categorical(x, num_classes=vocab_size) for x in X3])
y = to_categorical(Y3, num_classes=id_size)

# define model
del model
model = Sequential()
model.add(Dense(700, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(id_size, activation='softmax'))
print(model.summary())

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=10, verbose=1)

acc3 = compare_with_test(fold2)

print((acc1+acc2+acc3)/3)

#%%


#%%
