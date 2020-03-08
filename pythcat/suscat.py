import pandas as pd
import numpy as np


def suscat(df, columns, n = 1, num = 'percent'):
    """
    Detect suspected erroneous numeric data in user chosen columns of a dataframe

     Parameters
        ----------
        df : Pandas dataframe object
        col : list or array of column indices for which to test for suspected erroneous data
        n : integer value for amount of suspected values to return
        type : {'percent', 'number'}
            This optional parameter specifies whether n is a number of rows or percentage
            of values:

            * percent: interpret n as a percentage of rows in the df,
                Value must be between 0 <= n <= 100.
            * number: interpret n as a number of rows to return as suspected values.
                Value must be between 0 < n <= df.shape[0]

    Returns
    -------
    dictionary with key as index of column and values as row indices of suspected erroneous values

    Examples
    --------
>>>    suscat(pd.DataFrame({'Age': [2, 23, 4, 11], 'Number': [11, 99, 23, 8]}), columns = [1], n = 2, type = 'percent')
     {1: [1,3]}
    """

    # add input tests
    # check input value type
    if not isinstance(df, pd.DataFrame):
        raise Exception("A data frame object should be passed in the df argument")

    if num not in {'percent', 'number'}:
        raise Exception("type argument should be one of these values {'percent', 'number'}")

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
        alpha = n/100
    elif num == 'number':
        alpha = (n+1)/((df.shape[0])+1)
    for i in columns:
        # isolate relevant column
        a = df.iloc[:, i]
        # find upper quantile value
        h = np.quantile(a, 1-(alpha/2))
        # find lower quantile value
        l = np.quantile(a, alpha/2)
        # extract indices through boolian comparison to the quantile values
        temp = np.sort(np.append(np.argwhere((a < l).to_numpy()).flatten(), np.argwhere((a > h).to_numpy()).flatten()))

        output_dict[i] = temp

    return output_dict
