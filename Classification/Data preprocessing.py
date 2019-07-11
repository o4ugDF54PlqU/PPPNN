

#%%
# load text
input_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Raw Data\\"
output_path = "C:\\Users\\iD Student\\Documents\\PPNN\\Processed Data\\"
in_filename = 'multiuser_tweets.txt'

sentences = []
with open(input_path + in_filename, encoding="utf8") as myfile:
    line_count = 0
    for line in myfile:
        row = line.split("\t")
        if line_count == 0:
            line_count+=1
        elif line_count == 5000:
            break
        else:
            try:
                low = row[2].lower()
                sentences.append([int(row[0]),low])
                line_count+=1
            except:
                sentences[len(sentences)-1][1] = sentences[len(sentences)-1][1] + " " + row[0]
    print(f'Processed {line_count} lines.')

#%%
# organize into sequences of characters
sequences = list()
for tweet in sentences:
    words = tweet[1].split()
    if len(words) >= 5:
        for i in range(len(words)-4):
            seq = [words[i],words[i+1],words[i+2],words[i+3],words[i+4]]
            sequences.append([tweet[0],seq])

print('Total Sequences: %d' % len(sequences))
sequences

#%%
# save sequences to file
import pickle
filename = 'multi_user_WL5.txt'
out_filename = output_path+filename
pickle.dump(sequences, open(out_filename, "wb"))

#%%
