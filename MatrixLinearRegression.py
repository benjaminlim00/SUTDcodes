import numpy as np

X = np.array([[1, 4], [1, 5], [1, 6], [1, 7], [1,8], [1,9]])
y = np.array([[65], [71], [73], [74], [77], [79]])
θ = ((np.linalg.inv(X.T.dot(X))).dot(X.T)).dot(y)
print(θ)