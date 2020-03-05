import pandas as pd
def topcorr(df, k='all'):
    """
    Computes the dataframe with the top k correlated pairs of features

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
      The input dataframe
    k : int, default = 5
      The number of top correlated features 

    Returns
    -------
    pandas.core.frame.DataFrame
      The dataframe of top k correlated features
    """
    drop_pair = list()
    n_features = df.shape[1]
    n_pair = (n_features**2 - n_features) / 2

    for i in range(n_features):
        for j in range(i, n_features):
            drop_pair.append((df.columns[i], df.columns[j]))
    
    corr_df = df.corr().abs().unstack().drop(labels = drop_pair).sort_values(ascending=False)
    corr_df = pd.DataFrame(corr_df).reset_index()

    col_name = ['Feature 1', 'Feature 2', 'Absolute Correlation']
    corr_df.columns = col_name
    
    if k == "all":
        return corr_df
    else:
        return corr_df[:k]
