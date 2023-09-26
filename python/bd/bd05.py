import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn import metrics

boston = load_boston()
x_train, x_test, y_train, y_test =\
    train_test_split(boston.data, boston.target, test_size=0.3, random_state=12)

alpha = 0.1
ridge = Ridge(alpha=alpha)
ridge.fit(x_train, y_train)
ridge_predict = ridge.predict(x_test)

mse = metrics.mean_squared_error(y_test, ridge_predict)
mae = metrics.mean_absolute_error(y_test, ridge_predict)
print('MSE: {0:.3f}'.format(mse))
print('MAE: {0:.3f}'.format(mae))

r2_train = ridge.score(x_train, y_train)
r2_test = ridge.score(x_test, y_test)
print('Training-datasset R2 : {0:.3f}'.format(r2_train))
print('Test-datasset R2 : {0:.3f}'.format(r2_test))

ridge_coef_table = pd.Series(data=np.round(ridge.coef_, 1),
                             index=boston.feature_names)
print('Ridge Regression Coefficients:')
print(ridge_coef_table.sort_values(ascending=False))

plt.figure(figsize=(10, 5))
ridge_coef_table.plot(kind='bar')
#plt.ylim(-12, 5)
plt.show()

alphas = [0, 0.1, 0.12, 0.2, 0.5, 1, 10]

for a in alphas:
    ridge = Ridge(alpha = a)
    ridge.fit(x_train, y_train)
    ridge_y_pred = ridge.predict(x_test)

    mse = metrics.mean_squared_error(y_test, ridge_y_pred)
    rmse = np.sqrt(mse)

    r2_train = ridge.score(x_train, y_train)
    r2_test = ridge.score(x_test, y_test)

    print('Training-datasset R2 : {0:.3f}'.format(r2_train))
    print('Alpha:{0:.3f}, R2(train):{1:.3f}, R2(test):{2:.3f}, MSE:{3:.3f}, RMSE:{4:.3f}'
          .format(a, r2_train, r2_test, mse, rmse))


from sklearn.linear_model import Lasso

alpha = 0.1
lasso = Lasso(alpha=alpha)
lasso.fit(x_train, y_train)
lasso_predict = lasso.predict(x_test)

mse = metrics.mean_squared_error(y_test, lasso_predict)
mae = metrics.mean_absolute_error(y_test, lasso_predict)
print('MSE: {0:.3f}'.format(mse))
print('MAE: {0:.3f}'.format(mae))

r2_train = lasso.score(x_train, y_train)
r2_test = lasso.score(x_test, y_test)
print('Training-datasset R2 : {0:.3f}'.format(r2_train))
print('Test-datasset R2 : {0:.3f}'.format(r2_test))

lasso_coef_table = pd.Series(data=np.round(lasso.coef_, 1),
                             index=boston.feature_names)
print('Lasso Regression Coefficients:')
print(lasso_coef_table.sort_values(ascending=False))

plt.figure(figsize=(10,5))
lasso_coef_table.plot(kind='bar')
#plt.ylim(-10, 4)
plt.show()


alphas = [0, 0.1, 0.12, 0.2, 0.5, 1, 10]

for a in alphas:
    ridge = Ridge(alpha = a)
    ridge.fit(x_train, y_train)
    ridge_y_pred = ridge.predict(x_test)

    mse = metrics.mean_squared_error(y_test, ridge_y_pred)
    rmse = np.sqrt(mse)

    r2_train = ridge.score(x_train, y_train)
    r2_test = ridge.score(x_test, y_test)

    print('Training-datasset R2 : {0:.3f}'.format(r2_train))
    print('Alpha:{0:.3f}, R2(train):{1:.3f}, R2(test):{2:.3f}, MSE:{3:.3f}, RMSE:{4:.3f}'
          .format(a, r2_train, r2_test, mse, rmse))
