import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = np.loadtxt("data/train.csv", dtype="object", delimiter=",")

print(data)

train_X = pd.DataFrame(data[1:,:-1], columns=data[0,:-1])

print(train_X)

encoder=OneHotEncoder(sparse_output=False)

train_X_encoded = pd.DataFrame (encoder.fit_transform(train_X[['Compound']]))

train_X_encoded.columns = encoder.get_feature_names_out(['Compound'])

train_X.drop(['Compound'] ,axis=1, inplace=True)

OH_X_train= pd.concat([train_X, train_X_encoded ], axis=1)

print(OH_X_train)