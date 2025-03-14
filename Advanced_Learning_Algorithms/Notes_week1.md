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
$$a_n^{[2]}= g(\vec{w_n} \cdot \vec{a^{[2]}} + b_n)$$

Later it does a prediction, 
> is $\vec{a^{[2]}}$ >= 0.5
if yes then y = 1, if  no y=0

# More Complex Neural Networks

So, we're not just stopping at one hidden layer! Now we're talking about networks with multiple layers stacked on top of each other.

Imagine a picture going through a series of filters. Each filter (layer) picks out more and more complex features.

The video shows an example with **four layers** (not counting the input layer as Layer 0). Layers 1, 2, and 3 are **hidden layers**, and Layer 4 is the **output layer**. Remember, when people say a network has a certain number of layers, they usually mean the hidden layers plus the output layer.

Let's zoom into one of these hidden layers, say **Layer 3**. It takes the output from the previous layer (Layer 2) as its input. Let's call the output of Layer 2 as $\vec{a^{[2]}}$. Layer 3 then does some calculations and spits out its own output, $\vec{a^{[3]}}$.

**What's happening inside Layer 3?**

Let's say Layer 3 has three neurons (or "hidden units"). Each neuron does a similar calculation as we saw before:

For the first neuron:
$a_1^{[3]} = g(w_1^{[3]} \cdot \vec{a^{[2]}} + b_1^{[3]})$

For the second neuron:
$a_2^{[3]} = g(w_2^{[3]} \cdot \vec{a^{[2]}} + b_2^{[3]})$

For the third neuron:
$a_3^{[3]} = g(w_3^{[3]} \cdot \vec{a^{[2]}} + b_3^{[3]})$

Where:
- $w_i^{[3]}$ is the weight vector for the $i$-th neuron in Layer 3.
- $b_i^{[3]}$ is the bias for the $i$-th neuron in Layer 3.
- $\vec{a^{[2]}}$ is the output vector from the previous layer (Layer 2).
- $g$ is the activation function (like the sigmoid function we saw earlier).
- $a_i^{[3]}$ is the activation (output) of the $i$-th neuron in Layer 3.

The output of Layer 3, $\vec{a^{[3]}}$, is just a vector containing the activations of all its neurons: $[\begin{matrix} a_1^{[3]} \\ a_2^{[3]} \\ a_3^{[3]} \end{matrix}]$.

**The Notation Deep Dive**

To keep things organized, we use these little superscripts in square brackets to indicate the layer number (like $[3]$ for Layer 3) and subscripts to indicate the neuron index (like $_2$ for the second neuron).

So, $a_j^{[l]}$ means the activation of the $j$-th neuron in the $l$-th layer. Similarly, $w_j^{[l]}$ and $b_j^{[l]}$ are the weights and bias for the $j$-th neuron in the $l$-th layer.

Notice how the input to Layer 3, $\vec{a^{[2]}}$, comes from the *previous* layer (Layer 2). That's why in the formula, we're doing a dot product of the weights of Layer 3 with the activations of Layer 2.

**General Formula**

We can write a general formula for the activation of the $j$-th neuron in the $l$-th layer:

$a_j^{[l]} = g(w_j^{[l]} \cdot \vec{a^{[l-1]}} + b_j^{[l]})$

See how the input is $\vec{a^{[l-1]}}$, which is the output from the layer before (layer $l-1$).

**Activation Function: The "Go" Signal**

The function $g$ here is called the **activation function**. It decides whether a neuron should "fire" or not based on the input it receives. We've seen the sigmoid function, but there are other activation functions too (we'll learn about them later!).

**Making it Even More Consistent**

To make our notation super clean, we can even call the original input vector $X$ as $\vec{a^{[0]}}$. This way, the same formula works for the very first hidden layer (Layer 1) as well! When $l=1$, the formula becomes:

$a_j^{[1]} = g(w_j^{[1]} \cdot \vec{a^{[0]}} + b_j^{[1]})$

Which makes perfect sense because the first hidden layer takes the original input $\vec{a^{[0]}} (= X)$ as its input.

**Inference Algorithm: Making Predictions**

Now we know how to calculate the output of each layer given the output of the previous layer and the layer's parameters (weights and biases). This gives us the basic idea of how a neural network makes predictions! We feed the input through the network, layer by layer, until we get the final output from the output layer. This process is called **inference**.

Next up, we'll see how to put all this together into a step-by-step process for making predictions with a neural network!




