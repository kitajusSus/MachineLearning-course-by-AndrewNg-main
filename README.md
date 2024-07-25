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

## Unsupervised Learning part 1
Most used type of learning is the unsupervised learning. Is super just like supervised learning. hi hi. The main change is that (basing on the last example with tumor) we dont tell for algotith what is what. Algorithnm is just grouping the data in clusters thats why the main unsupervised Machine learning algorithm is called Clustering instead of ... idk somehthing else. Example of this algorithm is google news articles. They group the articles based on the similar data/words/dates in this articles that may be related one to another. 
![alt text](images\google_news.png)

Algorithm is finding words which exist simultaniously in every news, later on is just clustering these words  togther in groups or clusters. again idk how to call it exacly, but I'm trying okay???

MR. ANDREW SAID THAT THERE IS NOT EVEN ONE EMPLOYE IN GOOGLE WHO IS JUST  GROUPING THE WORDS IN NEWS FR??? 