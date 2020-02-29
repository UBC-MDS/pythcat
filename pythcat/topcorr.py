def topcorr(df, k):
    """
    Computes the dataframe with the top k correlated pairs of features

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
      The input dataframe
    k : int, default = 5
      The number of top correlated features 

    Returns
    -------
    pandas.core.frame.DataFrame
      The dataframe of top k correlated features
    """
