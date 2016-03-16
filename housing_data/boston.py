""" 
Load Boston Housing Prices Dataset from sklearn
and export into csv file
"""

import sklearn
import numpy as np
from sklearn.datasets import load_boston
import pandas as pd

#Load Boston data from sklearn
boston = load_boston()
df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
df.to_csv('out.csv',delimiter='\n',columns=df.columns, index=False)

