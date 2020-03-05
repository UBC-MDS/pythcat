from pythcat import topcorr
import pandas as pd
import numpy as np
import pytest

def test_inputs():
  """
  test whether the exception is raised when the input type and values are wrong
  """
  test_df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
  # test incorrect dataframe type
  with pytest.raises(Exception):
    topcorr.topcorr(1, 1)
  
  # test incorrect k type
  with pytest.raises(Exception):
    topcorr.topcorr(test_df, "1")
  
  # test when k is larger than number of feature pairs 
  with pytest.raises(Exception):
    topcorr.topcorr(test_df, 5)
  
  # test when k is a negative number
  with pytest.raises(Exception):
    topcorr.topcorr(test_df, -1)  
  
  # test when k is zero 
  with pytest.raises(Exception):
    topcorr.topcorr(test_df, 0)  
  
def test_outputs():
  """
  test whether the outputs type, shape and values are correct 
  """
  test_df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
  test_df_2 = pd.DataFrame([(.2, .3, .4), (.0, .6, .7), (.6, .0, .9), (.2, .1, .1)], columns=['x', 'y', 'z'])

  
  # test when k is default 
  result_1 = topcorr.topcorr(test_df)
  assert result_1.shape == (1, 3)
  assert result_1.equals(pd.DataFrame({'Feature 1': ['y'], 'Feature 2': ['x'], 'Absolute Correlation' : [1.0]}))
  
  # test when k is not default and equal to number of feature pairs
  result_2 = topcorr.topcorr(test_df)
  assert result_2.shape == (1, 3)
  assert result_2.equals(pd.DataFrame({'Feature 1': ['y'], 'Feature 2': ['x'], 'Absolute Correlation' : [1.0]}))
  
  # test when k is not default and less than number of feature pairs
  result_3 = topcorr.topcorr(test_df_2, 1)
  assert result_3.shape == (1, 3)
  assert np.allclose(result_3.iloc[0,2], 0.851064)

  
