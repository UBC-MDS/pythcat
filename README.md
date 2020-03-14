<img src="img/python_logo.jpg" width="200" align = "right">

## pythcat 

![](https://github.com/UBC-MDS/pythcat/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pythcat/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pythcat) ![Release](https://github.com/UBC-MDS/pythcat/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pythcat/badge/?version=latest)](https://pythcat.readthedocs.io/en/latest/?badge=latest)

Python package to simplify and ease EDA process.

*Creators: Netanel Barasch, Eithar Elbasheer, Yingping Qian, Hanying Zhang*

### Project Overview
`pythcat` is a package that provides a collection of convenient functions for Exploratory Data Analysis (EDA). In the early stage of a data science project, EDA is a crucial stage to perform an initial investigation on the dataset and inspire valuable research questions. This package simplifies the process of detecting and dealing with missing and suspicious values, as well as finding the relevant features. 

### Functions
The following 4 functions are included in our package.

1. `misscat`: This function drops rows if the number of the missing values exceeds the input threshold.

2. `suscat`: Datasets could include erroneous values such as outliers. This function detects suspected erroneous numeric data in user-chosen columns.

3. `repwithna`: Datasets could include uninformative strings, such as strings with only punctuations or blank strings. This function replaces these strings with `NA` so they can be removed as missing values.
        
4. `topcorr`: This function calculates the correlation between the columns and generates a list of top-correlated features in the dataset. 

### How `pythcat` fit in the python ecosystem
Several packages in the Python ecosystem could be used to either identify or deal with missing and erroneous values, such as [pandas](https://pandas.pydata.org), [pandas profiling](https://github.com/pandas-profiling/pandas-profiling), [numpy](https://numpy.org). However, it normally takes lines of code with a combination of these functions. Our packages will instead provide a simple and easy way to deal with these noise values in the data analysis. Some packages, such as [Altair](https://altair-viz.github.io) and  [Seaborn](https://seaborn.pydata.org), can be used to plot the correlation matrix for the dataset. The function in our package will generate a clear and easy-to-read list of top-correlated features instead of a correlation matrix. 

### Installation:

```
pip install -i https://test.pypi.org/simple/ pythcat
```

### Documentation
The official documentation is hosted on Read the Docs: <https://pythcat.readthedocs.io/en/latest/>

### Usage

The examples used below are based on iris from sklearn build in datasets. For demo purpose, we will insert some missing and erroneous values into this dataset.

```
from sklearn import datasets
import pandas as pd
import numpy as np
iris = datasets.load_iris()["data"]
iris = pd.DataFrame(iris, columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"])
iris.iloc[0,1:3] = np.NAN
iris.iloc[4,1:3] = np.NAN
iris.iloc[3,3] = 200
iris.iloc[4,3] = ""
iris = iris.head(5)
iris
```

The example dataframe is shown below:

|sepal_length|sepal_width|petal_length|petal_width|
|---|---|---|---|
|5.1|NaN |NaN |0.2|
|4.7 |3.2 |1.3 |0.2||
|4.6 |3.1|1.5|0.2|
||NaN|NaN|0.2|

### 1. misscat

**Arguments**

- df, the input data frame (pandas.core.frame.DataFrame)
- threshold, ratio of missing values to drop the row (float)

**Returns**:  
 a pandas dataframe after dropping the rows exceeded the threshold of missed values.

**Examples**

```
from pythcat.pythcat import misscat
misscat(df = iris, threshold = 0.4)

```

output will be:

|sepal_length|sepal_width|petal_length|petal_width|
|---|---|---|---|
|4.9	|3.0	|1.4	|0.2|
|4.7	|3.2	|1.3	|0.2|
|4.6	|3.1	|1.5	|200|



### 2. suscat

suscat(df, columns, n = 1, num = ‘percent’)

**Arguments**

- df, the input data frame (pandas.core.frame.DataFrame)
- columns, a list or array of column indices for which to test for suspected erroneous data (list)
- n, an integer value for the amount of suspected values to return (int)
num, the optional parameter specifies whether n is a number of rows or percentage (str)

**Returns** :  
dictionary with key as index of column and values as row indices of suspected erroneous values

**Examples**

```
from pythcat.pythcat import suscat
suscat(iris, columns = [3], n = 2)
```
output will be

{3: array([3])}

### 3. repwithna

**Arguments**

- df, the input data frame (pandas.core.frame.DataFrame)

**Returns**

a dataframe after replacing the uninformative string with NA (data.frame)

**Examples**

```
from pythcat.pythcat import repwithna
repwithna(df = iris)

```

output will be:

|sepal_length|sepal_width|petal_length|petal_width|
|---|---|---|---|
|5.1|NaN |NaN |0.2|
|4.7 |3.2 |1.3 |0.2||
|4.6 |3.1|1.5|0.2|
|NaN|NaN|NaN|0.2|

### 4. topcorr

**Arguments**

- df, the input data frame (pandas.core.frame.DataFrame)
- k, the number of feature pairs to return (int or str, default: “all”)

Generates a pandas dataframe with the top k correlated pairs of features

**Examples**

```
from pythcat.pythcat import topcorr
iris = datasets.load_iris()["data"]
iris = pd.DataFrame(iris, columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"])
topcorr(iris, 2)
```

output will be:

|Feature 1|Feature 2|Absolute Correlation|
|---|---|---|
|petal_length |petal_width |0.9629|
|petal_length|sepal_length|0.8718|

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
