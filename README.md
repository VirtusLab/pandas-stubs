# Pandas Stubs

Collection of Pandas [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files>) initially generated using [stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py), fixed when necessary and then partially completed.

## Motivation

Provide rudimentary coverage of Pandas code by static type checking, to alleviate problems mentioned in the following issues [14468](https://github.com/pandas-dev/pandas/issues/14468), [26766](https://github.com/pandas-dev/pandas/issues/26766). This approach was taken to achieve accelerated development - compared to refactoring existing Pandas codebase creating stub files is relatively uninhibited. 

Due to extensive Pandas API, quality of the proposed annotations is, for the most part, not suitable for integration into original codebase, but they can be very useful as a way of achieving some type safety during development.

## Installation and usage

The easiest way is using PyPI. This will add `.pyi` files to `pandas` package location, which will be removed when uninstalling:
```
pip install pandas-stubs
```

Alternatively, if you want a cleaner `PYTHONPATH` or wish to modify the annotations, manual options are:

* cloning the repository along with the files, or
* including it as a submodule to your project repository,

and then configuring a type checker with the correct paths.

## Pandas Version Compatibility

The aim of the current release is to cover the most common parts of the 1.0.4 API, however it can provide partial functionality for other version as well. Future versions will cover new Pandas releases.

### Versioning

The versions follow a pattern `MAJOR.MINOR.PATCH.STUB_VERSION` where the first three parts correspond to a specific Pandas API version, while `STUB_VERSION` is used to distinguish between the versions of the stubs themselves.

## Type checkers

As of now Mypy is the only type checker the stubs were tested with. 

## Testing

Test the stub files internal consistency:

```
mypy --config-file mypy.ini third_party/3/pandas
```

Test the stub files against actual code examples (this will use the stubs from the `third_party/3/pandas` dir):

```
mypy --config-file mypy.ini tests/snippets
```

Test the **installed** stub files against actual code examples (this will use Pandas .pyi files from your env):

```
mypy --config-file mypy_env.ini tests/snippets
```