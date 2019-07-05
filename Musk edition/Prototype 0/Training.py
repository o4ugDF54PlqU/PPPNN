
#%%
from numpy import array
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
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
in_filename = 'elon0_sequences_strict.txt'
raw_text = load_doc(input_path+in_filename)
lines = raw_text.split('\n')

#%%
chars = sorted(list(set(raw_text)))
mapping = dict((c, i) for i, c in enumerate(chars))

#%%
sequences = list()
for line in lines:
	# integer encode line
	encoded_seq = [mapping[char] for char in line]
	# store
	sequences.append(encoded_seq)

#%%
# vocabulary size
vocab_size = len(mapping)
print('Vocabulary Size: %d' % vocab_size)

#%%
sequences = array(sequences)
print(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
print(y)

#%%
sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
X = array(sequences)
y = to_categorical(y, num_classes=vocab_size)

#%%
# gpu check
import tensorflow as tf
with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

with tf.Session() as sess:
    print (sess.run(c))
from keras import backend as K
K.tensorflow_backend._get_available_gpus()

#%%
# define model
model = Sequential()
model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

#%%
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=15, verbose=2)

#%%
# save the model to file
model.save(input_path+'model0_strict.h5')
# save the mapping
dump(mapping, open(input_path+'mapping0_strict.pkl', 'wb'))

#%%
print("aaa")
#%%
