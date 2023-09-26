from re import L
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

boston = load_boston()
x_train, x_test, y_train, y_test =\
    train_test_split(boston.data, boston.target, test_size=0.3, random_state=12)

regression = LinearRegression()
regression.fit(x_train, y_train)
y_pred = regression.predict(x_test)

weight = np.round(regression.coef_, 1)
bias =  np.round(regression.intercept_, 2)
print('weight: ', weight)
print('bias: ', bias)

coef_table = pd.Series(data=weight, index=boston.feature_names)
print(coef_table.sort_values(ascending=False))

mse = metrics.mean_squared_error(y_test, y_pred)
mae = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print('MSE: {0:.3f}'.format(mse))
print('MAE: {0:.3f}'.format(mae))
print('RMSE: {0:.3f}'.format(rmse))
print('MAPE: {0:.3f}'.format(mape))

r2_score = regression.score(x_test, y_test)
r2_metric = metrics.r2_score(y_test, y_pred)

print('R-squared(r2_score) : {0:.3f}'.format(r2_score))
print('R-squared(r2_metric) : {0:.3f}'.format(r2_metric))
