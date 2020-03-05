from pythcat import repwithna
import pandas as pd
import numpy as np
import pytest

def test_repwithna():
    assert repwithna.repwithna(pd.DataFrame([['to?', '%@#$!!']]), rmvpunc=True).equals(pd.DataFrame([['to?', np.nan]])), "The strings with punctuations are not replaced properly."
    assert repwithna.repwithna(pd.DataFrame([['   ', ' 7 ']])).equals(pd.DataFrame([[np.nan, ' 7 ']])), "The empty strings are not replaced properly."
    assert repwithna.repwithna(pd.DataFrame([['Tom', 'tom'], ['Tina', 'Tinam']]), format="^T.*m$").equals(pd.DataFrame([['Tom', np.nan], [np.nan, 'Tinam']])), "The strings that are incompatible with the format are not replaced properly."

    with pytest.raises(Exception):
        repwithna.repwithna(['Tom', 'tom'])

    with pytest.raises(Exception):
        repwithna.repwithna(pd.DataFrame([['Tom', 'tom']]), rmvpunc='True')

    with pytest.raises(Exception):
        repwithna.repwithna(pd.DataFrame([['Tom', 'tom']]), format=12)