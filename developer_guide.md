## General rules for contribution

We warmly welcome any contribution to the project, and we try to make reviews on regular basis. Here is the short
guide, which hopefully will help you with starting. 

We use master-only git branch configuration. In order to merge your pull request into our main branch, you will need
at least one approval from one of the Code Owners (X or X). We tend to use the following labels to better describe
PR's: `CI`, `enhancement`, `bug` and `documentation`. In order to help with identifying problem you are solving, you might
also want to label pull request with pandas version it affects (`1.0`, `1.1` or `1.2`). 

## Repository organisation



## Tools and dependencies

We use [CircleCi](https://circleci.com/) to provide continuous integration and delivery for our project. 
The script with the whole configuration is `.circleci/config/yml`. It runs the following checks on each
pull request: tox verification against python 3.6, 3.7, 3.8, 3.9 versions and tests snippets from `tests/snippets`.
Additionally, on each merge to master branch, tests run again and new version of library is released. 

We use [tox](https://tox.readthedocs.io/en/latest/) to manage automatic `mypy` checks against our whole codebase.
Tox allows running checks with different python environments, and we use following ones: 3.6, 3.7, 3.8, 3.9. 
You don't need all of them installed locally, because tox will just warn about missing environment. However, there is
slight chance of your code being incompatible with one of the other Python versions. If so, you will be notified when 
tests run as part of pull request verification. 

We strongly suggest that each improvement you make and each buf you fix, have a corresponding example in `tests/snippets`.
This is our preferred way to make sure we cover corner cases of `pandas` library and that we keep backward compatibility. 
Some of our snippets test `pandas` interaction with other libraries such as `matplotlib` or `pyarrow`. All requirements
needed to make all tests passing are in `tests/requirements.txt`. Test snippets should be run with [pytest](https://docs.pytest.org/en/6.2.x/):

```
pytest tests
```