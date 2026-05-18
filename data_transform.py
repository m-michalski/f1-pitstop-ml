import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = np.loadtxt("data/train.csv", dtype="object", delimiter=",")

print(data)

train_X = pd.DataFrame(data[1:,:-1], columns=data[0,:-1])

print(train_X)

encoder=OneHotEncoder(sparse_output=False)

columns_to_change = ['Compound', 'Race', 'Year']

for i in range(len(columns_to_change)):
    
    train_X_encoded = pd.DataFrame (encoder.fit_transform(train_X[[f'{columns_to_change[i]}']]))
    train_X_encoded.columns = encoder.get_feature_names_out([f'{columns_to_change[i]}'])
    train_X.drop([f'{columns_to_change[i]}'] ,axis=1, inplace=True)
    OH_X_train= pd.concat([train_X, train_X_encoded ], axis=1)
    train_X = OH_X_train

train_X.drop(['id'] ,axis=1, inplace=True)
train_X.drop(['Driver'] ,axis=1, inplace=True)

train_X = train_X.astype(float)

print(train_X)