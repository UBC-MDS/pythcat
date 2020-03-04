import pandas as pd
import numpy as np
def misscat(df, threshold):
    """
    Drops rows or columns containing missing values if the number of the missing values exceeds a threshold

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    The input dataframe
    threshold : float
    The threshold of the missing values ratio needed to drop rows or columns 

    Returns
    -------
    pandas.core.frame.DataFrame
    dataframe of after dropping missing values.
    """
    if type(df) is not type(pd.DataFrame()):
        raise AssertionError("Data Must be a pandas dataframe")
    if type(threshold) is not int and type(threshold) is not float:
        raise AssertionError("threshold must a number")
    if float(threshold) < 0 or float(threshold) > 1:
        raise AssertionError("threshold must be between 0 and 1") 
        
    missing_rows = (df.isna().mean(axis = 1) > float(threshold)) 
    missing_index = df.index[missing_rows]
    df.drop(df.index[missing_index], inplace = True)