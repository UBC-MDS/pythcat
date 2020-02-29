def suscat(df, col = [], n = 0.01):
    """
    Detect suspected erroneous numeric data in user chosen columns of a dataframe
    
    :param df: dataframe like object
    :param col: list or array of column index's to check
    :param n: number of percentage of values to identify as potentially erroneous
    :return: dict, key as the column index and values is a list of row indecies.
    """   