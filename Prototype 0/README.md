# Prototype 0
*Note: to run any of these, you will have to modify the variable input_path and output_path in all the files* 
## Char level
This is the second version of the network (technically third, but I have decided that timeline is no longer canon). At this point, it is a simple character level generator consisting of a LSTM layer then a dense layer. 

**preparing data.py:** Run this first, it processes the data in the folder Raw Data and also determines the size of the input and ouput for the network later on. The default is 10 characters input and 1 output, 11 total.

**Training.py:** This script defines the model and trains it. Currently it defines a LSTM layer of size 75 and a dense layer of the size of the vocabulary of characters (around 70). It then saves the model as model0_strict.h5 and the mapping (to decode the output) as mapping0_strict.pkl.

**generation.py:** Finally, this script takes in the output of Training.py and uses it to generate the text. The script defines a function generate_seq which takes in the model, mapping, size of input (should be the same size as trained, smaller or larger may cause errors), the input (a start for the generator), and the size of output to output an output string. 3 examples included at the end.

## Word level
After doing the Char level network, I noticed that given a large output (50 or more characters), you can find that the network begins to fall into a predictable pattern no matter the input. I believe this is due to the limited dictionary of a character level network. To address this limitation, I modified the network into using world level generation. Since words are permutations of characters, this would multiply the size of the dictionary and hopefully increase the variations in output.

**WL preparing data.py:** Like preparing data.py in char level, but processes data into 2 words input and 3 output, 5 total. I also experimented with having different sizes of input and output, because I though having more than one output would give more interesting results that may may reveal deeper connections between each word. In the end, these experiments were inconclusive and abandoned due to time constraints and only the first output was used. Though this would be one of the top things that I would work on if I hypothetically (unlikely) came back to this. 

**WL Training.py:** Like the char level version, this script defines the model and trains it. The biggest difference is that it defines a LSTM layer of size 1000 instead of 70 and the vocab size is now 7500 - another way I tried to reduce the predictability of the char level, though at the cost of performance. It then saves the model as model_WL1.h5 and the mapping (to decode the output) as mapping_WL1.pkl.

**WL generation.py:** Exactly like the char level version, except now all the numbers refer to words instead of characters.

