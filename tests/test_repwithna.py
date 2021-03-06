from pythcat import pythcat
import pandas as pd
import numpy as np
import pytest


def test_repwithna():
    """
    tests whether exceptions are correctly raised
    and outputs are correctly returned.
    """

    # test cases
    df_1 = pd.DataFrame([['to? ', '%@#$!!']])
    df_2 = pd.DataFrame([['to? ', '   ']])
    df_3 = pd.DataFrame([['to? ', 'Tom']])
    output = pd.DataFrame([['to? ', np.nan]])

    # test whether strings with only
    # symbols are replaced correctly
    assert pythcat.repwithna(df_1, rmvsym=True).equals(output),\
        "The strings with symbols are not replaced properly."

    # test whether blank strings are replaced correctly
    assert pythcat.repwithna(df_2).equals(output),\
        "The empty strings are not replaced properly."

    # test whether strings that are not in the
    # customized format are replaced correctly
    assert pythcat.repwithna(df_3, format="^to.*").equals(output),\
        "The strings that are incompatible\
        with the format are not replaced properly."

    # tests for incorrect inputs (which should throw exceptions)
    # test when data is not passed as data frame
    with pytest.raises(Exception):
        pythcat.repwithna(['Tom', 'tom'])

    # test when `rmvsym` passed is not a boolean value
    with pytest.raises(Exception):
        pythcat.repwithna(pd.DataFrame([['Tom', 'tom']]), rmvsym='True')

    # test when `format` passed is not a string
    with pytest.raises(Exception):
        pythcat.repwithna(pd.DataFrame([['Tom', 'tom']]), format=12)
