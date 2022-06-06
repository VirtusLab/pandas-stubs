<p align="center">
<img src="https://raw.githubusercontent.com/VirtusLab/pandas-stubs/master/logo.png"
     alt="Logo"
     width="60%"/>
</p>  

# Pandas Stubs

Collection of pandas [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files>) initially generated using [stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py), fixed when necessary and then partially completed.

|CI|PyPi version | PyPI Downloads | Conda Downloads | Python support | License
|--|--|--|--|--|--|
| [![VirtusLab](https://circleci.com/gh/VirtusLab/pandas-stubs.svg?style=svg)]() | [![PyPI package](https://img.shields.io/pypi/v/pandas-stubs.svg)](https://pypi.org/project/pandas-stubs) | [![PyPI download month](https://img.shields.io/pypi/dm/pandas-stubs.svg)](https://pypi.python.org/pypi/pandas-stubs/) | [![PyPI download month](https://anaconda.org/conda-forge/pandas-stubs/badges/downloads.svg)](https://anaconda.org/conda-forge/pandas-stubs)  | [![PyPI pyversions](https://img.shields.io/pypi/pyversions/pandas-stubs.svg)](https://pypi.python.org/pypi/pandas-stubs/)|[![GitHub license](https://img.shields.io/github/license/VirtusLab/pandas-stubs.svg)](https://github.com/VirtusLab/pandas-stubs/blob/master/LICENSE)

# Announcement - pandas_stubs is moving! 

**Starting from July 2022 `pandas_stubs` package will no longer be sourced from here
but instead from a repository owned and maintained by the core pandas team:**
https://github.com/pandas-dev/pandas-stubs

This is result of a strategic effort lead by the core pandas team to integrate [Microsoft type stub repository](https://github.com/microsoft/python-type-stubs)
together with the [current pandas_stubs repository](https://github.com/VirtusLab/pandas-stubs).

All future development will take place in the new repository and both the PyPI and CondaForge distributions will be sourced from there.

If you're having any problems with the current package please try switching over, and report any issues on the new Github page. Direct pip install and conda are still unsupported but try the following command:
```
pip install git+https://github.com/pandas-dev/pandas-stubs
```
or just clone the repository manually and specify it in `mypy.ini`.

Related issue: [172](https://github.com/VirtusLab/pandas-stubs/issues/172)

## Motivation
Provide rudimentary coverage of pandas code by static type checking, to alleviate problems mentioned in the following issues [14468](https://github.com/pandas-dev/pandas/issues/14468), [26766](https://github.com/pandas-dev/pandas/issues/26766). This approach was taken to achieve accelerated development - compared to refactoring existing Pandas codebase creating stub files is relatively uninhibited. 

Due to extensive pandas API, quality of the proposed annotations is, for the most part, not suitable for integration into original codebase, but they can be very useful as a way of achieving some type safety during development.

## Installation

The easiest way is using PyPI. This will add `.pyi` files to `pandas` package location, which will be removed when uninstalling:
```
pip install pandas-stubs
```

Another way to install is using Conda:

```
conda install -c conda-forge pandas-stubs 
```

Alternatively, if you want a cleaner `PYTHONPATH` or wish to modify the annotations, manual options are:

* cloning the repository along with the files, or
* including it as a submodule to your project repository,

and then configuring a type checker with the correct paths.

## Usage

Let’s take this example piece of code in file `round.py`

```
import pandas as pd

decimals = pd.DataFrame({'TSLA': 2, 'AMZN': 1})
prices = pd.DataFrame(data={'date': ['2021-08-13', '2021-08-07', '2021-08-21'],
                            'TSLA': [720.13, 716.22, 731.22], 'AMZN': [3316.50, 3200.50, 3100.23]})
rounded_prices = prices.round(decimals=decimals)
```

Mypy won't see any issues with that, but after installing pandas-stubs and running it again:

```
mypy round.py
```

we get the following error message:

```
round.py:6: error: Argument "decimals" to "round" of "DataFrame" has incompatible type "DataFrame"; expected "Union[int, Dict[Union[int, str], int], Series]"
```

And after confirming with the [docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html)
we can fix the code:

```
decimals = pd.Series({'TSLA': 2, 'AMZN': 1})
```

## Version Compatibility

The aim of the current release is to cover the most common parts of the 1.2.0 API, however it can provide partial functionality for other version as well. Future versions will cover new Pandas releases.

### Versioning

The versions follow a pattern `MAJOR.MINOR.PATCH.STUB_VERSION` where the first three parts correspond to a specific pandas API version, while `STUB_VERSION` is used to distinguish between the versions of the stubs themselves.

## Type checkers

As of now mypy is the only type checker the stubs were tested with.

## Development

### Testing using tox

Tox will automatically run all types of tests mentioned further.
It will create isolated temporary environments for each declared version of Python and install `pandas-stubs`
like it would normally be installed when using pip or conda.

Usage is as simple as:

```
tox
```

Last few lines of the output should look like this (assuming all Python versions are available):
```
  pep8: commands succeeded
  py36: commands succeeded
  py37: commands succeeded
  py38: commands succeeded
  py39: commands succeeded
```

### Partial testing

Test the stub files internal consistency:

```
mypy --config-file mypy.ini third_party/3/pandas
```

Test the stub files against actual code examples (this will use the stubs from the `third_party/3/pandas` dir):

```
mypy --config-file mypy.ini tests/snippets
```

Test the **installed** stub files against actual code examples.
You'll need to install the library beforehand - the .pyi files from your env will be used:

```
mypy --config-file mypy_env.ini tests/snippets
```

Test if the code examples work, when actually ran with pandas:

```
pytests tests/snippets
```

# Disclaimer
This project provides additional functionality for [pandas](https://pandas.pydata.org/docs/index.html) library. Pandas is available under it's own [license](https://github.com/pandas-dev/pandas/blob/master/LICENSE).

This project is not owned, endorsed, or sponsored by any of AQR Capital Management, NumFOCUS, LLC, Lambda Foundry, Inc. and PyData Development Team.
