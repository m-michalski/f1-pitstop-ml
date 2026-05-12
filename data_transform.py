import numpy as np

data = np.loadtxt("data/train.csv", dtype="object", delimiter=",")
print(f'Shape of the data: {data.shape}\n')

X = data[1:,:-1]
y = data[1:,-1]

print(f'Nr of samples: {(X.shape)[0]}\nNr of features: {(X.shape)[1]}')
print(f'Nr of labels: {(y.shape)[0]}')

drivers = np.unique(X[:,1])
compounds = np.unique(X[:,2])
races = np.unique(X[:,3])
years = np.unique(X[:,4])

print(f'Nr of unique drivers: {(drivers.shape)[0]}\nUnique drivers:\n{drivers}\n')
print(f'Nr of unique compounds: {(compounds.shape)[0]}\nUnique compounds:\n{compounds}\n')
print(f'Nr of unique races: {(races.shape)[0]}\nUnique races:\n{races}\n')
print(f'Nr of unique years: {(years.shape)[0]}\nUnique years:\n{years}\n')

X_float = X[:,5:].astype(dtype="float")
