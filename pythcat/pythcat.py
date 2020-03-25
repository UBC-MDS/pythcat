import pandas as pd
import numpy as np


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
    >>> data = pd.DataFrame(data = {"X": [1, None, 2],
    "Y": [2, None, None], "Z": [1, 2, None]})
    >>> pythcat.misscat(data, threshold = 0.3)
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
    dictionary with key as index of column and values as array of row indices
    of suspected erroneous values

    Examples
    --------
    suscat(pd.DataFrame({'Age': [2, 23, 4, 11], 'Number': [11, 99, 23, 8]}),
    columns = [1], n = 2, num = 'number')
    > {1: [1,3]}

    suscat(pd.DataFrame({'Age': [2, 23, 4, 11], 'Number': [11, 99, 23, 8]}),
    columns = [1], n = 25, num = 'percent')
    > {1: [2]}
    """

    # add input tests
    _input_test_suscat(df, columns, n, num)

    output_dict = {}

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


def _input_test_suscat(df, columns, n=1, num='percent'):
    # helper function to test suscat input
    # df type
    if not isinstance(df, pd.DataFrame):
        raise Exception("A dataframe object should be passed as df")
    # check num value
    if num not in {'percent', 'number'}:
        raise Exception("type should one of these {'percent', 'number'}")
    # check n value
    if n != int(n):
        raise Exception("n should be an integer ")
    elif num == 'percent' and (n > 100 or n < 0):
        raise Exception("a percentage should be between 0 and 100")
    elif num == 'number' and (n > df.shape[0]):
        raise Exception("Can't return more then df.shape[0]")
    # check columns type
    if not isinstance(columns, list):
        raise Exception("col argument should be list of column indices")


def repwithna(df, rmvsym=False, format=None):
    """
    Replace uninformative strings (eg. empty strings like '') in the
    data frame with NAs, so they can be removed as missing values.
    By default, empty strings will be replaced. If 'rmvsym' is set
    to 'True', strings containing only symbols will also be
    replaced. If 'format' is set with a regular expression, the
    function will replace all the strings of non-compliant formats
    with NAs.

    Parameters
    ----------
    df: pandas.core.frame.DataFrame
      The input dataframe
    rmvsym: boolean, default=False
      If True, remove all the strings containing only symbols
    format: String, default=None
      A regular expression representing the format of the string value
      in the data frame

    Returns
    -------
    pandas.core.frame.DataFrame
      The new dataframe with uninformative strings replaced as NAs

    Examples
    --------
    >>> data = pd.DataFrame([['Momo', 23], ['momo', 11]],
        columns = ['Name', 'Age'])
    >>> pythcat.repwithna(data, format='^M.+')
        Name  Age
        Momo   23
        NaN   11
    """

    # check input value type
    if not isinstance(df, pd.DataFrame):
        raise Exception("A data frame should be passed to\
      replace the uninformative strings with NAs.")

    if not isinstance(rmvsym, bool):
        raise Exception("'rmvsym' should be a boolean value.")

    if format is not None and not isinstance(format, str):
        raise Exception("The format should be a regular expression.")

    if format is None:
        # replace empty string with NAs
        df = df.replace(r'^\s*$', np.nan, regex=True)
        # replace strings with only symbols with NAs(if it is asked)
        if rmvsym:
            df = df.replace(r'^[!"#$%&\'()*+,-.\/:;<=>?@[\\\]^_`{|}~]*$',
                            np.nan, regex=True)
    else:
        # replace strings that are not in the customized format with NAs
        remove = '^(?!' + format + ').*$'
        df = df.replace(remove, np.nan, regex=True)
    return df


def topcorr(df, k="all", method='pearson'):
    """
    Generates a pandas dataframe with the top k correlated pairs of features

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
      The input dataframe
    k : str or int, default = 'all'
      if k is an int, it is the number of top correlated feature pairs;
      if 'all', display all the pairs of features based on absolute correlation
    method : str, default = 'pearson'
      method of correlation, can be either ‘pearson’, ‘kendall’, or ‘spearman’

    Returns
    -------
    pandas.core.frame.DataFrame
      The dataframe of top k correlated features

    Examples
    --------
    >>> data = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
    >>> pythcat.topcorr(data, 1)
        Feature 1 Feature 2  Absolute Correlation
        y         x                   1.0
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("The input df should be a Pandas data frame!")

    n_features = df.shape[1]
    n_pair = (n_features ** 2 - n_features) / 2

    if k != "all" and not isinstance(k, int):
        raise Exception("The input k should be 'all' or a positive integer!")

    if k != "all":
        if k <= 0:
            raise Exception("The input k should be a positive integer!")
        if k > n_pair:
            raise Exception("The input k should be less than number of pairs!")

    drop_pair = list()

    for i in range(n_features):
        for j in range(i, n_features):
            drop_pair.append((df.columns[i], df.columns[j]))

    corr_df = df.corr(method=method).abs().round(4).unstack()
    corr_df = corr_df.drop(labels=drop_pair).sort_values(ascending=False)
    corr_df = pd.DataFrame(corr_df).reset_index()
    col_name = ['Feature 1', 'Feature 2', 'Absolute Correlation']
    corr_df.columns = col_name
    if k == "all":
        return corr_df
    else:
        return corr_df[:k]
