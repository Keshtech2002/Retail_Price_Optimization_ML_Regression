import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

# Generic function to get price elasticities
def create_model_and_find_elasticity(data):
    model = ols("QUANTITY ~ PRICE", data).fit()
    price_elasticity = model.params[1]

    # Print out price Elasticity and model summary
    print('Price elasticiy of the product: ' + str(price_elasticity))
    print(model.summary())

    # Create plot for model
    fig = plt.figure(figsize=(12, 8))
    fig = sm.graphics.plot_partregress_grid(model, fig=fig)

    # Return model and price_elasticity of the product
    return model, price_elasticity