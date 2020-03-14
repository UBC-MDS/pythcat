# tests misscat.py
import pandas as pd
from pythcat import pythcat
import pytest


# Testing the misscat() function
def test_misscat():
    # Create a testing dataframe
    data = pd.DataFrame(data={"X": [1, None, 2], "Y": [2, None, None],
                              "Z": [1, 2, None]})
    # testing the number of dropped rows
    output = pythcat.misscat(data, 0.5)
    assert output.shape[0] == 1
    # Tests if an exception has been raised when
    # a non dataframe is passed to the function
    with pytest.raises(Exception):
        pythcat.misscat(df=1, threshold=0.3)
    # Tests if an exception has been raised when
    # a threshold higher than 1 is passed
    with pytest.raises(Exception):
        pythcat.misscat(df=data, threshold=2)
    # Tests if an exception has been raised when
    # a threshold less than 0 is passed
    with pytest.raises(Exception):
        pythcat.misscat(df=data, threshold=-0.1)
    # Tests if an exception has been raised when
    # a non numeric datatype is passed for the threshold
    with pytest.raises(Exception):
        pythcat.misscat(df=data, threshold="0.3")
