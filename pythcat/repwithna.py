def repwithna(df):
    """
    Replace uninformative strings (eg. empty strings like '') in the data frame with NAs, 
    so they can be removed as missing values.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
      The input dataframe

    Returns
    -------
    pandas.core.frame.DataFrame
      The new dataframe with uninformative strings replaced as NAs

    Examples
    --------
    >>> repwithna(df)
    """