import pandas as pd


def misscat(df, threshold):
    """
    Drops rows containing missing values if the number
    of the missing values exceeds a threshold

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
      The input dataframe
    threshold : float
      The threshold of the missing values ratio needed to drop rows

    Returns
    -------
    pandas.core.frame.DataFrame
      dataframe of after dropping missing values

    Examples
    ---------
    >>> from pythcat.misscat import misscat
    >>> data = pd.DataFrame(data = {"X": [1, None, 2],
    "Y": [2, None, None], "Z": [1, 2, None]})
    >>> misscat.misscat(data, threshold = 0.3)
        X    Y    Z
        1.0  2.0  1.0
    """
    if not isinstance(df, pd.DataFrame):
        raise AssertionError("Data must be a pandas dataframe")
    if type(threshold) is not int and type(threshold) is not float:
        raise AssertionError("threshold must be a number")
    if float(threshold) < 0 or float(threshold) > 1:
        raise AssertionError("threshold must be between 0 and 1")

    missing_rows = (df.isna().mean(axis=1) > float(threshold))
    missing_index = df.index[missing_rows]

    return df.drop(df.index[missing_index])
