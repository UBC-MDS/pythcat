import pandas as pd
import numpy as np


def repwithna(df, rmvpunc=False, format=None):
    """
    Replace uninformative strings (eg. empty strings like '') in the
    data frame with NAs, so they can be removed as missing values.
    By default, empty strings will be replaced. If 'rmvpunc' is set
    to 'True', strings containing only punctuations will also be
    replaced. If 'format' is set with a regular expression, the
    function will replace all the strings of non-compliant formats
    with NAs.

    Parameters
    ----------
    df: pandas.core.frame.DataFrame
      The input dataframe
    rmvpunc: boolean, default=False
      If True, remove all the strings containing only punctuations
    standard: String, default=None
      A regular expression representing the format of the string value
      in the data frame

    Returns
    -------
    pandas.core.frame.DataFrame
      The new dataframe with uninformative strings replaced as NAs

    Examples
    --------
    >>> repwithna(pd.DataFrame([['  ',  23], [',;/', 11]],
    >>>   columns = ['Name', 'Age']), rmvpunc=True)
      Name   | Age   |
    ------------------
      NaN    |  23   |
    ------------------
      NaN    |  11   |
    ------------------
    """

    # check input value type
    if not isinstance(df, pd.DataFrame):
        raise Exception("A data frame should be passed to\
      replace the uninformative strings with NAs.")

    if not isinstance(rmvpunc, bool):
        raise Exception("'rmvpunc' should be a boolean value.")

    if format is not None and not isinstance(format, str):
        raise Exception("The format should be a regular expression.")

    if format is None:
        # replace empty string with NAs
        df = df.replace(r'^\s*$', np.nan, regex=True)
        # replace strings with only punctuations with NAs(if it is asked)
        if rmvpunc:
            df = df.replace(r'^[!"#$%&\'()*+,-.\/:;<=>?@[\\\]^_`{|}~]*$',
                            np.nan, regex=True)
    else:
        # replace strings that are not in the customized format with NAs
        remove = '^(?!' + format + ').*$'
        df = df.replace(remove, np.nan, regex=True)
    return df
