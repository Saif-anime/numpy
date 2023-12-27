# The Normal Distribution is one of the most important distributions.

# It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.

# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

# Use the random.normal() method to get a Normal Data Distribution.

# It has three parameters:

# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.


from numpy import random

x = random.normal(size=(2, 3))

print(x)