# Prototype 1
*Note: to run any of these, you will have to modify the variable input_path and output_path in all the files* 
You should read the readme.md in prototype 0 before this as this builds upon it

**Date filter basic and preprocessing.py:** 

**Multi Training.py:** This script defines the model and trains it. Currently it defines a LSTM layer of size 75 and a dense layer of the size of the vocabulary of characters (around 70). It then saves the model as model0_strict.h5 and the mapping (to decode the output) as mapping0_strict.pkl.

**Auto generation.py:** Finally, this script takes in the output of Training.py and uses it to generate the text. The script defines a function generate_seq which takes in the model, mapping, size of input (should be the same size as trained, smaller or larger may cause errors), the input (a start for the generator), and the size of output to output an output string. 3 examples included at the end.

**Auto generation - TFIDF.py:** Finally, this script takes in the output of Training.py and uses it to generate the text. The script defines a function generate_seq which takes in the model, mapping, size of input (should be the same size as trained, smaller or larger may cause errors), the input (a start for the generator), and the size of output to output an output string. 3 examples included at the end.
