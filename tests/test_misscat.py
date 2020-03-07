# tests misscat.py
import pytest
import pandas as pd
from pythcat import misscat

# A testing data Frame
data = pd.DataFrame(data = {"X": [1, None, 2], "Y": [2, None, None], "Z": [1, 2, None]})

#
output = misscat.misscat(data, 0.5)
assert output.shape[0] == 1

with pytest.raises(Exception):
    misscat.misscat(df = 1, threshold = 0.3)
    
with pytest.raises(Exception):
    misscat.misscat(df = data, threshold = 2)
    
with pytest.raises(Exception):
    misscat.misscat(df = data, threshold = "0.3")