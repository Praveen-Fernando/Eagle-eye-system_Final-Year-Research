import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

# read data into a DataFrame
data = pd.read_csv('C:\\Users\\Praveen\\Desktop\\test.csv', index_col=0)
data.head()

# # create a fitted model
lm1 = smf.ols(formula='check ~ Robbery', data=data).fit()
# print(lm1.params)

### STATSMODELS ###

# create a fitted model with all three features
lm1 = smf.ols(formula='check ~ Robbery + Aggraveted_Assualt + Weapons_Dealing +	Mortor_vehicle_Theft +	Kidnapping_Cases +	Murder_cases +	Fighting_in_public', data=data).fit()

# print the coefficients
print(lm1.params)

# create X and y
feature_cols = ['Robbery', 'Aggraveted Assualt', 'Weapons Dealing',	'Mortor vehicle Theft',	'Kidnapping Cases',	'Murder cases',	'Fighting in public']
X = data[feature_cols]
y = data.check

# instantiate and fit
lm2 = LinearRegression()
lm2.fit(X, y)

# print the coefficients
print(lm2.intercept_)
print(lm2.coef_)

list(zip(feature_cols, lm2.coef_))

### STATSMODELS ###

# print a summary of the fitted model
print(lm1.summary())