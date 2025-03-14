# Neural Networks Intuition 
Lets say, that we have 1000x1000 pixel picture, and every (i,j) pixel has its own value, independent from each other. 
For Example, pixture is black/white, which means that enery (row, column) means the brightnes of the pixel. 
Later they said about making a whole picture as a 1 vector (1 kolumn and 1000000 rows. {every pixel from picture is now in one row}). 
When you train this on a lot of data, you can get less presice output if you want to recognize persons. 
Neurons can learn to recognize the special part of pixels e.x. nose, eye. 

*Output Layer* is going to create a picture based on known data and input data. 

Every layer is looking at a bit bigger part of picture. 

## Neural Network Intuition Quiz!!!
it wasnt difficult its not even necesary to write anything about this beside that:

1. Which of these reffer to components of Neural Network??
- neurons
- layers
- activation function

2. Neural networks take inspiration from, but do not very accurately mimic, how neurons in a biological brain learn.
- true



# Neural Network Layer.
HOW TO BUILD NEURAL NETWORK

**Layer 1**

$[\vec{w_n},  b_n] a_n= g(\vec{w_n} \cdot \vec{x} + b_n)$

We make this computation for Every data in our "vector".  

To make it easier g(z) function looks like this:

$$g(z) = \frac{1}{1+e^{-z}}$$

This all here are hidden Neurons

**Layer 2** 

*Input of layer 2 is output of Layer1*

And because Layer 2 has only one neuron, it means we do the same computation but only once. It a scalar value 
$$ a_n^{[2]}= g(\vec{w_n} \cdot \vec{a^{[2]}} + b_n)$$$
