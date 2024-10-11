# another week of studing ppl WELCOME WELCOME

# Feature Scaling in Gradient Descent
[link to the video from course](https://www.coursera.org/learn/machine-learning/lecture/KMDV3/feature-scaling-part-1)
## Introduction
- **Feature Scaling**: Technique to enable gradient descent to run much faster.
- **Example**: Predicting house price using two features:
    - `x1`: Size of the house (300 to 2000 square feet)
    - `x2`: Number of bedrooms (0 to 5)

## Parameter Values
- Example house: 2000 square feet, 5 bedrooms, price $500,000.
- Possible parameter values:
    - `w1 = 50`, `w2 = 0.1`, `b = 50`
        - Estimated price: $100,000k + $0.5k + $50k = $100,050k (far from actual price)
    - `w1 = 0.1`, `w2 = 50`, `b = 50`
        - Estimated price: $200k + $250k + $50k = $500k (matches actual price)

## Observations
- Large range of feature values (e.g., size in square feet) -> Small parameter value (e.g., `w1 = 0.1`)
- Small range of feature values (e.g., number of bedrooms) -> Large parameter value (e.g., `w2 = 50`)

## Impact on Gradient Descent
- Scatter plot: `x1` (size) on horizontal axis, `x2` (bedrooms) on vertical axis.
- Cost function contour plot:
    - Horizontal axis (narrow range, e.g., 0 to 1)
    - Vertical axis (large range, e.g., 10 to 100)
    - Contours form ellipses (tall and skinny)
- Small changes in `w1` (large impact on cost `J`)
- Large changes in `w2` (small impact on cost `J`)

## Feature Scaling
- **Purpose**: Transform training data so features take on comparable ranges.
- Example transformation:
    - `x1` and `x2` both range from 0 to 1
- Result:
    - Contours look more like circles
    - Gradient descent finds a more direct path to the global minimum

## Wnioski
jakoś leci i będzie [dobrze spokojnie powoli do przodu](https://www.youtube.com/watch?v=QPM2spkcSeM)

# Feature scaling PART 1###
Feature scaling is used to make faster predictions, ex:

$\text{price} = w_1x_1 + w_2x_2 +b$

$x_1$ is size of house in range 300 to 2000 ($ft^2$) (big numbers)

$x_2$ is a number of bedrooms in range 0 - 5  (small numbers)

And the problem is that, our numbers are not in similar range.
What is the size of parameters $w_1, w_2$ if aour training example is $x_1 = 2000$, $x_2= 5$, $price = $500k$ ???

$w_1 = 50, w_2= 0.1 , b=50$ after quick math we will find out that, our prediction is equal to $100 050.5**k** (It's much bigger number than ours real price which was $500k)

**Other posibility**
$w_1 = 0.1, w_2= 50 , b=50$ 
This model finds the value of house ~ $500k.
>more reasonable

![picture 1](images\image.png)

To avoid situations like this, when we get wrong parameters by our model, we can **scale the features**, to do this we use normalization, just like we do it in vector normalization. After the entire operation, once we have our parameters, we can restore them to their previous values if we want to (its not permament). If we use gradient descend  now with changed values we should get nice little circle. 

# Feature scaling part 2 :smile: yippie

How to scale features?

If we get $x_1$ in range $300<x_1<2000$ we just need to devide $x_1$ by the biggest posible value (2000)  $x_{1, scaled} = \frac{x_1}{2000}$, which gives us  $0.15<x_{1, scaled}<1$
 
nothing new. 11.10.2024
