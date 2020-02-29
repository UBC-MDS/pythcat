## pythcat 

![](https://github.com/EitharAlfatih/pythcat/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/EitharAlfatih/pythcat/branch/master/graph/badge.svg)](https://codecov.io/gh/EitharAlfatih/pythcat) ![Release](https://github.com/EitharAlfatih/pythcat/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pythcat/badge/?version=latest)](https://pythcat.readthedocs.io/en/latest/?badge=latest)

Python package to ease EDA for Catogorical variables.

### Project Overview
`pythcat` is a package that provides a collection of convenient functions for Exploratory Data Analysis (EDA). In the early stage of a data science project, EDA is a crucial stage to perform an initial investigation on the dataset and inspire valuable research questions. This package simplifies the process of detecting and dealing with missing and suspicious values, as well as finding the relevant features. 

### Functions
The following 4 functions are included in our package.

1. `misscat`: This function provides a summary of missing values in the dataset and drops rows or columns if the number of the missing values exceeds the input threshold.

2. `suscat`: Datasets could include erroneous values such as outliers. This function detects suspected erroneous numeric data in user-chosen columns.

3. `repwithna`: Datasets could include uninformative strings, such as strings with only punctuations or blank strings. This function replaces these strings with `NA` so they can be removed as missing values.
        
4. `topcorr`: This function calculates the correlation between the columns and generates a list of top-correlated features in the dataset. 

### How `pythcat` fit in the python ecosystem
TODO

### Installation:

```
pip install -i https://test.pypi.org/simple/ pythcat
```

### Features
- TODO

### Dependencies

- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://pythcat.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
