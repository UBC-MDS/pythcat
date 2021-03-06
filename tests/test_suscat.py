from pythcat import pythcat
import pandas as pd
import pytest


def test_inputs():
    """
    testing functionality of input checks
    """

    df = pd.DataFrame({'x': [1, 2, 11, 22, 8], 'y': [100, 110, 155, 200, 540]})
    # test df input
    with pytest.raises(Exception):
        pythcat.suscat([[1, 2, 3], [1, 2, 3]], [0])
    # test num input
    with pytest.raises(Exception):
        pythcat.suscat(df, [1], num="")
    # test n input
    with pytest.raises(Exception):
        pythcat.suscat(df, [1], n=1.1, num='number')
    with pytest.raises(Exception):
        pythcat.suscat(df, [1], n=20000000, num='number')
    with pytest.raises(Exception):
        pythcat.suscat(df, [1], n=200, num='percent')
    # test column input
    with pytest.raises(Exception):
        pythcat.suscat(df, '1')


def test_outputs():
    """
    testing correct functionality and outputs of function
    """

    df = pd.DataFrame({'x': [1, 2, 11, 22, 7], 'y': [100, 110, 120, 130, 140]})

    out1 = pythcat.suscat(df, [0, 1], n=80)
    out2 = pythcat.suscat(df, [0], num='number', n=2)

    assert isinstance(out1, dict)
    assert len(out1.keys()) == 2 and len(out1[1]) == 4
    assert max(out1[0]) <= len(df.loc[:, 'x']) and min(out1[0]) >= 0
    assert max(out1[1]) <= len(df.loc[:, 'y']) and min(out1[1]) >= 0
    assert len(out2.keys()) == 1 and len(out2[0]) == 2
