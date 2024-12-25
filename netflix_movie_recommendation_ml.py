# -*- coding: utf-8 -*-
"""Netflix Movie recommendation ML.ipynb

**Eclat**

Importing libraries
"""

!pip install apyori

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""Importing dataset"""

dataset = pd.read_excel('/content/NetfilxMovies.xlsx', header = None)
transactions = []

for i in range(0, 7466):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

"""**Eclat training on dataset**"""

from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.002, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

"""**Visualizing**

Raw results
"""

results = list(rules)
print(results)

"""Proper display"""

def inspect(results):
    movie_1 = [tuple(result[2][0][0])[0] for result in results]
    movie_2 = [tuple(result[2][0][1])[0] for result in results]
    support = [result[1] for result in results]
    return list(zip(movie_1, movie_2, support))
dataframe_intelligence = pd.DataFrame(inspect(results), columns = ['Movie 1', 'Movie 2', 'Support'])

dataframe_intelligence

dataframe_intelligence.nlargest(n = 15, columns = 'Support')
