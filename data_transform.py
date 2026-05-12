import numpy as np

data = np.loadtxt("data/train.csv", dtype="object", delimiter=",")
print(f'Shape of the data: {data.shape}\n')

X = data[1:,:-1]
y = data[1:,-1]

print(f'Nr of samples: {(X.shape)[0]}\nNr of features: {(X.shape)[1]}')
print(f'Nr of labels: {(y.shape)[0]}')

drivers = np.unique(X[1:,1])
compounds = np.unique(X[1:,2])
races = np.unique(X[1:,3])

print(compounds)

print(f'Nr of unique drivers: {(drivers.shape)[0]}\nUnique drivers:\n{drivers}\n')
print(f'Nr of unique compounds: {(compounds.shape)[0]}\nUnique compounds:\n{compounds}\n')
print(f'Nr of unique compounds: {(races.shape)[0]}\nUnique compounds:\n{races}\n')



