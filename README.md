# MachineLearning-course-by-AndrewNg
This repository contains my journey with the machine learning course by  AndrewNg from `coursera.com`
* sorry for my english descriptions 
# Chapter 1  **Supervised machine learning - Regresion and Clasification**
## What is machine learning?
>"Field of study that gives computers the ability to learn withour being explicitly programed" ~ Arthur Samuel (1959)

Because the computer gets posibilities to train the model all the time makes it easier to understand for himself the way for example to be better player at checkers. 
>"Training 10 times is less efficient than training 10000times and find your mistakes"

**Types of machine learning:**

* Supervised learning - (1st and 2nd part of the course)
* Unsuperviesed learning - (3-rd part of the course)
* Recommender systems
* Reinforcement learning

>Firsty you need to get set of tools and later on you will be able to study a way to efficient use of these. 

## Supervised learning 1

You give your learning algorithms inputs and outputs. By use this data algorithm learns from being given `right answers`

**Examples**
![alt text](/\image.png)
or 
![alt text](images/image-1.png)

### Regresion
When we are trying to predict optimal price for house based on size we can build the model which is using [x,y] => [size, price] to predict the price for every given size. Jutro like linear regresion ` y = ax+b` the algorithm is looking for `a` which is `arctan(y/x)`. After all calculations algorithm is making streight line, basing on this line we can predict the "optimal price" for a house based on it size.

**Regresion** - trying to predict a number infinitely many possible outputs.

## Supervised learning 2

### Classification
**Example** : breast cancer detection
We are making algorithm which is using clasiffication to look for malignant(really bad) or benign(not that bad) bazed on his size. \\
Plan:
* **Data Collection**: Gather medical records, including tumor characteristics.
* **Training**: The machine learning model is trained on labeled data, learning to differentiate between benign and malignant tumors.
* **Prediction**: For new patients, the model predicts the tumor class based on the input features.
![alt text](images/image-2.png)

**Classification** :
* predict categories of the tumor, using  0,1,2. 
* have small number of possible outputs.

### Two and more inputs
If we want to use more inputs for example 2 and now we use [[size, age],[diagnosis]] we are able to make more accurate model in making diagnosis.

### Sumary
**Supervised learning** maps the input `x` to the output `y`:
* learns from being given `right answers`

**Main types of supervised learning** : 
* regression - predict the numbers of infinitly many possible outputs
* Classification - predict categories of the small number of possible outputs. 

# Chapter 2
Hello cuties papoties today we gonna learn about (pls dont be scared) unsupervised learning method. POGCHAMP
## Unsupervised Learning part 1
Most used type of learning is the unsupervised learning. Is super just like supervised learning. hi hi. The main change is that (basing on the last example with tumor) we dont tell for algotith what is what. Algorithnm is just grouping the data in clusters thats why the main unsupervised Machine learning algorithm is called Clustering instead of ... idk somehthing else. 

Example of this algorithm is google news articles. They group the articles based on the similar data/words/dates in this articles that may be related one to another. 
![alt text](images/google_news.png)

Algorithm is finding words which exist simultaniously in every news, later on is just clustering these words  togther in groups or clusters. again idk how to call it exacly, but I'm trying okay???

MR. ANDREW SAID THAT THERE IS NOT EVEN ONE EMPLOYE IN GOOGLE WHO IS JUST  GROUPING THE WORDS IN NEWS FR??? 

**Unsupervised learning pros**
* you dont need to know what is what, all you need is for your data to have some specific features <numbers, words ... and so on>

### Clustering - grouping customers
Basing on given data (hobby of customers) the algorithm gives us the clusters of customers. 
![alt text](images/clustering.png)

## Unsupervised learning part 2

In unsupervised learning data only comes with inputs `x` but not outputs with labels `y`. Algorithm has to find structure in the data.

* Clustering :
    * group similar data
    * points together
* Anomaly detection
    * finds unusual data points
* Dimensionality reduction (we dont know what is this yet but we will eventually in the future)
    * Compress data using fewer numbers

## Jupyter Notebook 
 i use:
 * python 3.12.4
 * miniconda 3
 * [Jupyter testbook 1](ml_course.ipynb)

this program makes work with machine learning easier because you can work with every line of code and its easier to understand your work. 

# Linear regression model

## Linear regression model part 1
**Problem**: make prediction about price of the house basing on the size of the house. 

We will use: 
* Regresion model for predicting numbers

In this dataset, we get size in feet^2 and price of house in $1000's 

Notation is: 
* `x` = input variable feature (size of house)
* `y` = output variable, target variable (price of house)
**Single example** = (`x`,`y`)
**Training example** = (`x_(i)`, `y_(i)`) the i-th example (1nd, 2nd, 3rd, etc)


## Linear Regression model part 2 
 To build linear regression model, we need to have the following:
 * training set - it has features and targets needed to train our model our (x,y) pairs
 * then we go to learning algorithm 
 * f = our function  which is using new `x` to give us the  new `y` (or `y` with hat  is our prediction )based on the training data we done earlier. 

 `x` is called feature, `y` is called prediction (target)

for model on house price it will look like this:

**zise --> f --> price (estimated)**

### How to represent f? 

its asy bruhs:  `y = ax +b `, y(x)= ax+b

### Why we use linear  function when we want to draw streight line?
Because its relatyvley easy to work with, 

go to [JUPYTER NOTEBOOK 2](ml_course2.ipynb), I forgot to install a lot of libraries on this machine. womp womp situation fr. 

I had problem with vsc couse it didnt saw a packeges I installed. Solving of this problem was to install them by using the terminal,  in vsc not in anaconda cmd crazy moment sorry I didnt know, but now I do. 

## Linear regression - Cost Function
There is nothing important to do here, just simple math equations you can find it in the internet. 

Next video is about the visualisation of the cost function. ![eq](images/equasions.png)

# Visualisation examples
Optional Lab: 
[other notebook](ml_course3.ipynb)
Shows how to calculate the cost function and how to visualize with matplotlib, useful. thanks andrew uwu ng. 



# Gradient Descent
UUUUUUUUUUUUUUU POGCHAMP REAL MATH  INCOMIUNG. `pop smoke - dior is blasting rn`

## Gradient Descent algorithm 
![gradient](images/GRADIENT_EQ.png)

alfa - learning rate, how big step we take with learning
![eq3](images/eq3.png)
![eq4](images/eq4.png)

Learning rate is always a positive number!!!!!!!!!
![curve](images/curve.png)
i dont think that I need to show you what a tan(x) is???. 

NOW WE KNOW:

**Bias** is like a personal opinion or belief that a machine learning model has. It's like when you have a hunch or a gut feeling about something, even if you don't have any evidence. In machine learning, bias helps the model make predictions even when there's no input data. It's like the model's default guess or tendency.

**Weights** are like the importance or relevance that the model gives to different factors when making predictions. It's like when you consider some things more important than others when making a decision. In machine learning, weights are used to combine the input data in a smart way. Each input gets multiplied by its weight, and the results are added up to make a prediction.

I MADE CODE WITH GRADIENT  -----> [simple gradient code](gradient.py) <-----

# Learning rate parameter.

