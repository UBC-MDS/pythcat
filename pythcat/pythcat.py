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

def suscat(df, col = [], n = 0.01):
    """
    Detect suspected erroneous numeric data in user chosen columns of a dataframe
    
    :param df: dataframe like object
    :param col: list or array of column index's to check
    :param n: number of percentage of values to identify as potentially erroneous
    :return: dict, key as the column index and values is a list of row indecies.
    """   

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