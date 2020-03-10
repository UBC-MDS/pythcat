
from pythcat import repwithna
import pandas as pd
import numpy as np
import pytest


def test_repwithna():
    """
    tests whether exceptions are correctly raised
    and outputs are correctly returned.
    """

    df_1 = pd.DataFrame([['to? ', '%@#$!!']])
    df_2 = pd.DataFrame([['to? ', '   ']])
    df_3 = pd.DataFrame([['to? ', 'Tom']])
    output = pd.DataFrame([['to? ', np.nan]])

    # test for replacing strings with only punctuations
    assert repwithna.repwithna(df_1, rmvpunc=True).equals(output),\
        "The strings with punctuations are not replaced properly."

    # test for replacing blank strings
    assert repwithna.repwithna(df_2).equals(output),\
        "The empty strings are not replaced properly."

    # test for replacing strings that are not in the format
    assert repwithna.repwithna(df_3, format="^to.*").equals(output),\
        "The strings that are incompatible\
        with the format are not replaced properly."

    # tests for incorrect inputs (which should throw exceptions)
    with pytest.raises(Exception):
        repwithna.repwithna(['Tom', 'tom'])

    with pytest.raises(Exception):
        repwithna.repwithna(pd.DataFrame([['Tom', 'tom']]), rmvpunc='True')

    with pytest.raises(Exception):
        repwithna.repwithna(pd.DataFrame([['Tom', 'tom']]), format=12)
