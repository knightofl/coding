import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df_bike = pd.read_csv('./practice/bike_demand_kaggle.csv')
x_df_bike = df_bike.iloc[:, 5:9]

df_bike['y'] = 1
df_bike.loc[df_bike['count'] < 500, 'y'] = 0
y = df_bike['y']

scaler = StandardScaler()
scaler.fit(x_df_bike)
result = scaler.transform(x_df_bike)
x_scaled_bike = pd.DataFrame(data=result, columns=x_df_bike.columns)

x_train, x_test, y_train, y_test =\
    train_test_split(x_scaled_bike, y, test_size=0.3, random_state=12)

clf = LogisticRegression()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)


from sklearn.metrics import roc_curve

predict_prob = clf.predict_proba(x_test)
print('Predicted class probability', np.round(predict_prob[101], 3))
print('Target data index', y_test.values[101])

fprs, tprs, thresholds = roc_curve(y_test, predict_prob[:, 1])
print(thresholds.shape)
print(fprs.shape)
print(tprs.shape)

thr_index = np.arange(0, thresholds.shape[0], 110)
print('Sample Threshold Index(n=10):', thr_index)
print('Sample Threshold Value(n=10):', np.round(thresholds[thr_index], 2))
print('Sample Threshold FPR(n=10):', np.round(fprs[thr_index], 3))
print('Sample Threshold TPR(n=10):', np.round(tprs[thr_index], 3))


def roc_curve_plot(y_test , pred_proba_c1):
    import matplotlib.pyplot as plt
    fprs , tprs , thresholds = roc_curve(y_test ,pred_proba_c1)

    plt.plot(fprs , tprs, label='ROC')
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    
    start, end = plt.xlim()
    plt.xticks(np.round(np.arange(start, end, 0.1),2))
    plt.xlim(0,1); plt.ylim(0,1)
    plt.xlabel('FPR'); plt.ylabel('TPR( Recall )')
    plt.legend()
    plt.show()

roc_curve_plot(y_test, clf.predict_proba(x_test)[:, 1] )


from sklearn.metrics import roc_auc_score

roc_score = roc_auc_score(y_test, predict_prob[:, 1])
print('Testing Data AUC: {:0.3f}'.format(roc_score))