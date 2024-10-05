# another week of studing ppl WELCOME WELCOME

# Feature Scaling in Gradient Descent

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
