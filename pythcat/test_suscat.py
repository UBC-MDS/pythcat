from pythcat import suscat
import pandas as pd
import numpy as np
import pytest

def test_inputs():
    """
    testing functionality of input checks
    """

    df = pd.DataFrame({'x': [1, 2, 11, 22, 8], 'y': [100, 110, 155, 200, 540]})
    # test df input
    with pytest.raises(Exception):
        suscat.suscat([[1, 2, 3], [1, 2, 3]], [0])
    # test num input
    with pytest.raises(Exception):
        suscat.suscat(df, [1], num="")
    # test n input
    with pytest.raises(Exception):
        suscat.suscat(df, [1], n=1.1)
    # test column input
    with pytest.raises(Exception):
        suscat.suscat(df, 6)


def test_outputs():
    """
    testing correct functionality and outputs of function
    """

    df = pd.DataFrame({'x': [1, 2, 11, 22, 7], 'y': [100, 110, 120, 130, 140]})

    out1 = suscat.suscat(df, [0, 1], n=40)
    out2 = suscat.suscat(df, [0, 1], num='number', n=3)


    assert isinstance(out1, dict)
    assert len(out1.keys()) == 2 and len(out1.values()) == 2
    assert max(out1['x']) <= len(df.loc[:, 'x']) and min(out1['x']) >= 0
    assert max(out1['y']) <= len(df.loc[:, 'y']) and min(out1['y']) >= 0
    assert len(out1['x']) == 2
    assert len(out2['x']) == 3


