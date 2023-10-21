# Retail_Price_Optimization_ML_Regression
Implementing a retail price optimization algorithm using regression trees. One of the first steps to building a dynamic pricing model.
One of the ways machine learning has helped businesses is price optimization. It addresses a lot of problems that retailers face in their businesses Price optimization is a strategic approach used by businesses to determine the most effective and profitable pricing strategies for their products or services.
> “Your customer base won’t purchase your product if you price it too high, but your business won’t be able to cover expenses if you price it too low.”

### AIM
Provided with Restaurant Cafe data , we can leverage price elasticity with historical Cafe sales data to measure customers' responses to price changes and find the optimal price to set for their items for maximum profit i.e. striking a balance between low or high prices.

### Exploratory data analysis
- Any covariate with like SchoolBreak, Weekends that increases sales and has no effects on price are dropped since we are not interested in seeing effects on sales due to these covariates.
- Check for missing values.
- Uncovering multiple facets of merge data.

### Modellling
- Price elasticity of demand (PED) measure use to show the responsiveness of the quantity demanded of a good or services to changes in price when nothing else is change i.e relationship between demand and price. i.e the effective desire for something changes as price changes. It gives the % change in quantity for 1 % increase in price Mathematically The formula for the price elasticity (ǫ)
> $$ e = \frac{\Delta Q}{\Delta P}$$

- We will look at sales of Cafe that sales burgers, the Cafe owner wants to know the optimal price to set for their item in order to gain maximum profit. Note. If the prices are high, the sales will reduce and if the prices are low the sales will increase and hence total profit will decrease. So the task here is to get a sweet spot that will give us the maximum profit. So we are trying to find a linear relationship between quantity and price hence use a linear regression in this case

### Files and Description
| Files | Desrcription |
| ----- | ------------ |
| [Cafe_Price_Optimazation.ipynb](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/Cafe_Price_Optimazation.ipynb) | Price optimization notebook |
| [Demand_Forecasting.md](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/Demand_Forecasting.md) | Demand forecasting |
| [Dynamic_Pricing.md](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/Dynamic_Pricing.md) | Dynamic pricing |
| [Predictive_Aanalysis.md](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/Predictive_Aanalysis.md) | Predictive analysis |
| [Price_Optimiztaion.md](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/Price_Optimiztaion.md) | Price Optimization |
| [PriceElasticity.py](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/PriceElasticity.py) | functions to help in calcuating price elasticity |
| [OptimalPrice.py](https://github.com/Keshtech2002/Retail_Price_Optimization_ML_Regression/blob/main/OptimalPrice.py) | functions to help calculate optimal price |
