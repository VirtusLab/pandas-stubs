# PySpark Stubs

Collection of Pandas [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files>) initially generated using [stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py), fixed when necessary and then partially completed.

## Motivation

Provide minimal coverage of Pandas code by static type checking, to alleviate problems mentioned in the following issues [14468](https://github.com/pandas-dev/pandas/issues/14468), [26766](https://github.com/pandas-dev/pandas/issues/26766). This approach was taken to achieve accelerated development - compared to refactoring existing Pandas codebase creating stub files is relatively uninhibited. 

Due to extensive Pandas API, quality of the proposed annotations is, for the most part, not suitable for integration into original codebase, but they can be very useful as a way of achieving some type safety during development.

## Installation and usage

As of now, the only method of installation is either cloning the repository along with the files, or including it as a submodule, and then configuring a type checker with the correct paths.

Near-future plans involve releases to PyPI and conda-forge.

## Pandas Version Compatibility

The aim of the current release is to cover the most common parts of the 1.0.3 API. Future releases will cover new API versions.

## Type checkers

As of now Mypy is the only type checker the stubs were tested with.
