<img src="img/python_logo.jpg" width="200" align = "right">

## pythcat 

[![](https://github.com/EitharAlfatih/pythcat/workflows/build/badge.svg)] [![codecov](https://codecov.io/gh/EitharAlfatih/pythcat/branch/master/graph/badge.svg)](https://codecov.io/gh/EitharAlfatih/pythcat) ![Release](https://github.com/EitharAlfatih/pythcat/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pythcat/badge/?version=latest)](https://pythcat.readthedocs.io/en/latest/?badge=latest)

Python package to simplify and ease EDA process.

*Creators: Netanel Barasch, Eithar Elbasheer, Yingping Qian, Hanying Zhang*

### Project Overview
`pythcat` is a package that provides a collection of convenient functions for Exploratory Data Analysis (EDA). In the early stage of a data science project, EDA is a crucial stage to perform an initial investigation on the dataset and inspire valuable research questions. This package simplifies the process of detecting and dealing with missing and suspicious values, as well as finding the relevant features. 

### Functions
The following 4 functions are included in our package.

1. `misscat`: This function provides a summary of missing values in the dataset and drops rows or columns if the number of the missing values exceeds the input threshold.

2. `suscat`: Datasets could include erroneous values such as outliers. This function detects suspected erroneous numeric data in user-chosen columns.

3. `repwithna`: Datasets could include uninformative strings, such as strings with only punctuations or blank strings. This function replaces these strings with `NA` so they can be removed as missing values.
        
4. `topcorr`: This function calculates the correlation between the columns and generates a list of top-correlated features in the dataset. 

### How `pythcat` fit in the python ecosystem
Several packages in the Python ecosystem could be used to either identify or deal with missing and erroneous values, such as [pandas](https://pandas.pydata.org), [pandas profiling](https://github.com/pandas-profiling/pandas-profiling), [numpy](https://numpy.org). However, it normally takes lines of code with a combination of these functions. Our packages will instead provide a simple and easy way to deal with these noise values in the data analysis. Some packages, such as [Altair](https://altair-viz.github.io) and  [Seaborn](https://seaborn.pydata.org), can be used to plot the correlation matrix for the dataset. The function in our package will generate a clear and easy-to-read list of top-correlated features instead of a correlation matrix. 


[Altair](https://altair-viz.github.io), [Seaborn](https://seaborn.pydata.org) are usually used to plot correlation matrix between features, 

### Installation:

```
pip install -i https://test.pypi.org/simple/ pythcat
```

### Documentation
The official documentation is hosted on Read the Docs: <https://pythcat.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
