from pythcat import pythcat
import pandas as pd
import pytest

def test_output():
  """
  test if the output is correct if the correct type of values are input
  """
  df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
  results = pythcat.topcorr(df, 1)
  assert results.shape == (1, 3)
  
def test_wrong_input():
  """
  test if the input types are wrong
  """
  with pytest.raises(Exception):
    pythcat.topcorr(1, 1)
  
  with pytest.raises(Exception):
    pythcat.topcorr(1, "d")
  
