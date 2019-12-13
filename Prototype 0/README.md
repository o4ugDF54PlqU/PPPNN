# Prototype 0
*Note: to run any of these, you will have to modify the variable input_path and output_path* 
## Char level
This is the second version of the network. At this point, it is a simple character level generator consisting of a LSTM layer then a dense layer. 

**preparing data.py:** Run this first, it processes the data in the folder Raw Data and also determines the size of the input for the network later on. The default is 10 characters input and 1 output, 11 total.

**Training.py:** This script defines the model and trains it.
