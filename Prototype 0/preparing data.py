
#%%
import csv

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

# save tokens to file, one dialog per line
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()

#%%
# load text
input_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Raw Data\\"
output_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\"
in_filename = 'elonmusk_tweets.csv'

sentences = []
with open(input_path + in_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count+=1
        else:
            sentences.append(row[2][2:-1])
            line_count+=1
    print(f'Processed {line_count} lines.')
    
raw_text = " ".join(sentences)
print(raw_text)

#%%
# clean
tokens = raw_text.split()
tokens

#%%
len(tokens)

#%%
for word in tokens:
    if "/" in word or "\\" in word or "RT" in word or "@" in word:
        tokens.remove(word)
raw_text = ' '.join(tokens)
print(raw_text)

#%%
# organize into sequences of characters
length = 10
sequences = list()
for i in range(length, len(raw_text)):
    # select sequence of tokens
    seq = raw_text[i-length:i+1]
    # store
    sequences.append(seq)
print('Total Sequences: %d' % len(sequences))


#%%
sequences

#%%
# save sequences to file
filename = 'elon0_sequences_strict.txt'
out_filename = output_path+filename
save_doc(sequences, out_filename)


#%%
sequences

#%%
