
from sklearn import tree
import os
import numpy

# smooth = 1 and bumpy = 0
features = [[140, 1], [130, 1], [150, 0], [170, 0],
            [141, 1], [143, 1], [145, 1], [146, 0],
            [141, 1], [143, 1], [145, 1], [146, 0]]

# apple = 0 and oranges = 1
labels = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]

# making the custom classifier
adoreclassifier = tree.DecisionTreeClassifier()


# Fitting values to a DecisionTreeClassifier
adoreclassifier = adoreclassifier.fit(features, labels)

prediction = adoreclassifier.predict([[142, 1]])

# giving clear outputs to identify here

print()
