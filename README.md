# PPPNN
Personalized Password Prediction Neural Network Proof of Concept

Included are multiple RNNs made to train and identify a person's style of writing and thoughts based off of their tweets. Early versions are merely LSTM text generators and the later ones try to generate something that is closer to a password.

Why is this a thing?

I believe that with enough data, a person's conscious mind can be modeled and closely replicated. This project is also meant to make users more aware and careful with the amount of private information that they post online while companies needs to be more careful about how their user's data is handled.

This project attempts to prove this concept, by trying to predict a person's password based off of the information on them that is publicly available. Currently, the network only uses Twitter posts as the input data since it is publicly available and there is a large amount of data contained in them. 

However, that is still a small dataset with not a lot of information. A malicious actor could easily create a network and feed it even more data that is not publicly or legally available online, such as a person's previously leaked and cracked passwords, massively increasing the accuracy of the network. 

Such a technique can be considered an evolution over traditional credential stuffing attacks, though the neural network inference will mean an increase in the time and energy cost of each attempt. This will likely limit the neural network method to individual, high value targets such as system administrators, government officials, or celebrities.

Nonetheless, the use of multi-factor security devices and randomly generated password strings (stored in password managers) would thwart any malicious actor using this method, which is why no one important should use a single, legible password to protect their accounts. 
