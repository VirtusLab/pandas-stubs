"""
Setup for Pandas type annotations.
For the sake of convenience the package installation
will coexist with Pandas installation.
If this is a problem - download the source
and add it to PYTHONPATH manually.
"""

from setuptools import setup
import os

version = "1.2.0.29"


# find_packages might not work with stub files
src_path = os.path.join("third_party", "3")


def list_packages(source_path: str = src_path) -> None:
    for root, _, _ in os.walk(os.path.join(source_path, "pandas")):
        yield ".".join(os.path.relpath(root, source_path).split(os.path.sep))


setup(
    name="pandas-stubs",
    package_dir={"": src_path},
    version=version,
    description="Type annotations for Pandas",
    long_description=(open("README.md").read()
                      if os.path.exists("README.md") else ""),
    long_description_content_type='text/markdown',
    url="https://github.com/VirtusLab/pandas-stubs",
    packages=list(list_packages()),
    package_data={"": ["*.pyi", "py.typed"]},
    license="MIT",
    author="Zbigniew Królikowski",
    author_email="zkrolikowski@virtuslab.com",
    install_requires=[
        'typing_extensions>=3.7.4.3;python_version<"3.8"'
    ],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Typing :: Typed",
    ],
)
