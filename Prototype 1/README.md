# Prototype 1
*Note: to run any of these, you will have to modify the variable input_path and output_path in all the files* 

You should read the readme.md in prototype 0 before this as this builds upon it

**Date filter basic and preprocessing.py:** An improved version of the script used in Prototype 0. The tweet's date is now added to each individual tweet after processing, allowing for certain date ranges to be filtered out. This can be useful when the attacker knows when a password was created. The data can be narrowed down to the weeks around the password creation date - allowing for better representation of the target's thoughts and, by extention, their password.

**Multi Training.py:** The first half of this script is copied from the character level version. After that, the network takes in the tweets filtered between april and may and trains the already trained model on it with a lower epoch. In theory, this should bias the model towards this time period more, while keeping the larger context outside this time period - which simply filtering would get rid of. It then saves the model as 2_stage_proto_model.h5 and the mapping (to decode the output) as 2_stage_proto_mapping.pkl.

**Auto generation.py:** 

**Auto generation - TFIDF.py:**
