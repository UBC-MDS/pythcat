def missing(df, threshold):
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