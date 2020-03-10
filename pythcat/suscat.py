import pandas as pd
import numpy as np


def suscat(df, columns, n=1, num='percent'):
    """
    Detect suspected erroneous numeric data in user
    chosen columns of a dataframe

    Parameters
    ----------
    df : Pandas dataframe object
    col : list or array of column indices for which to test for
        suspected erroneous data
    n : integer value for amount of suspected values to return
    type : {'percent', 'number'}
        This optional parameter specifies the whether n is a
        number of rows or percentage of values:


        * percent: interpret n as a percentage of rows in the df,
            Value must be between 0 <= n <= 100.
        * number: interpret n as a number of rows of suspected values.
            Value must be between 0 < n <= df.shape[0]

    Returns
    -------
    dictionary with key as index of column and values as row indices of
    suspected erroneous values

    Examples
    --------
    suscat(pd.DataFrame({'Age': [2, 23, 4, 11], 'Number': [11, 99, 23, 8]}),
    columns = [1], n = 2, type = 'percent')
    > {1: [1,3]}
    """

    # add input tests
    # check input value type
    if not isinstance(df, pd.DataFrame):
        raise Exception("A dataframe object should be passed as df")

    if num not in {'percent', 'number'}:
        raise Exception("type should one of these {'percent', 'number'}")

    if n != int(n):
        raise Exception("n should be an integer ")

    if not isinstance(columns, list):
        raise Exception("col argument should be list of column indices")

    output_dict = {}
    if n > df.shape[1] and num == 'number':
        n = df.shape[1]
    if n > 100 and num == 'percent':
        n = 100
    if num == 'percent':
        alpha = n / 100
    elif num == 'number':
        alpha = (n + 1) / ((df.shape[0]) + 1)
    for i in columns:
        # isolate relevant column
        col = df.iloc[:, i]
        # find upper quantile value
        high = np.quantile(col, 1 - (alpha / 2))
        # find lower quantile value
        low = np.quantile(col, alpha / 2)
        # extract indices through boolean comparison to the quantile values
        high_i = np.argwhere((col > high).to_numpy()).flatten()
        low_i = np.argwhere((col < low).to_numpy()).flatten()
        temp = np.sort(np.append(low_i, high_i))

        output_dict[i] = temp

    return output_dict
