import pandas as pd
def topcorr(df, k='all'):
  """
  Generates a pandas dataframe with the top k correlated pairs of features

  Parameters
  ----------
  df : pandas.core.frame.DataFrame
    The input dataframe
  k : int, default = 'all'
    The number of top correlated feature pairs
    Display all the pairs of features based on absolute correlation if 'all' 

  Returns
  -------
  pandas.core.frame.DataFrame
    The dataframe of top k correlated features
  
  Examples
  --------
  >>> df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
  >>> topcorr(df, 1)
  """
  if not isinstance(df, pd.DataFrame):
    raise Exception("The input df should be a Pandas data frame!")
  
  n_features = df.shape[1]
  n_pair = (n_features**2 - n_features) / 2
  
  if k != "all" and not isinstance(k, int):
    raise Exception("The input k should be 'all' or an integer!")
  
  if k > n_pair:
    raise Exception("The input k should be an integer less than number of pairs!")
    
  drop_pair = list()
  
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
