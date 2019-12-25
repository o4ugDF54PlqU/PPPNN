# Prototype 1
*Note: to run any of these, you will have to modify the variable input_path and output_path in all the files* 

You should read the readme.md in prototype 0 before this as this builds upon it

## Date filter basic and preprocessing.py
An improved version of the script used in Prototype 0. The tweet's date is now added to each individual tweet after processing, allowing for certain date ranges to be filtered out. This can be useful when the attacker knows when a password was created. The data can be narrowed down to the weeks around the password creation date - allowing for better representation of the target's thoughts and, by extention, their password.

## Multi Training.py
The first half of this script is copied from the word level version of Prototype 0. After that, the network takes in the tweets filtered between april and may and trains the already trained model on it with a lower epoch. In theory, this should bias the model towards this time period more, while keeping the larger context outside this time period - which simply filtering would get rid of. It then saves the model as 2_stage_proto_model.h5 and the mapping (to decode the output) as 2_stage_proto_mapping.pkl.

## Auto generation.py
The generate_seq function from the previous versions is kept unchanged in this script. The main difference here is that after the function definition, instead of using the function directly, I incorporated gensim and NLTK to select the most important word to act as the starter.

This improvement attempts to change the attack from brute forcing the password by randomly choosing a starting point to selectively targeting starting points/topics that are most likely to be correct.

This required me to create a dictionary counting nouns from the tweet dataset, removing the stopwords which are included in NLTK, then using gensim to build a word2vec model. The model and the dictionary are then combined to find topics that are used most often - indicating that the target thinks about this topic a lot and therefore more likely to base their password on. The word/topic that has the highest score will then be passed to generate_seq, and in a real world scenario, if the password (and its variants like adding capitalization, 123 at the end, etc) is incorrect then the generator would move on to the next highest scoring word/topic.

## Auto generation - TFIDF.py
This version tries to avoid brute forcing like the above, but by using TF-IDF rather than my own custom solution. 

I don't remember if I ever got this to work correctly, especially since I just saw a syntax error that would've prevented it from working when I made it. Though it's still possible it works (all the logic seems correct), I wouldn't know since my current machine doesn't have Gensim, NLTK, keras, TensorFlow, etc installed anymore and can't check. Installing TF to use GPU is such a hassle. So if you got it working, let me know and I'll update this.
