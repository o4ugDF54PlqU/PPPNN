
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
            low = row[2][2:-1].lower()
            sentences.append(low)
            line_count+=1
    print(f'Processed {line_count} lines.')
    
raw_text = " ".join(sentences)
print(sentences)

#%%
# clean
count = 0
for tweet in sentences:
    temp = tweet.split()
    for word in temp:
        if '/' in word:
            temp.remove(word)
        elif '\\' in word:
            temp.remove(word)
        elif 'rt' in word:
            temp.remove(word)
        elif '@' in word:
            temp.remove(word)
    sentences[count] = temp
    count += 1
sentences

#%%
# organize into sequences of characters
sequences = list()
for tweet in sentences:
    for i in range(len(tweet)-4):
        seq = tweet[i]+" "+tweet[i+1]+" "+tweet[i+2]+" "+tweet[i+3]+" "+tweet[i+4]
        sequences.append(seq)
print('Total Sequences: %d' % len(sequences))
sequences
#%%
# save sequences to file
filename = 'elon_sequences_WL1.txt'
out_filename = output_path+filename
save_doc(sequences, out_filename)


#%%
sequences

#%%
