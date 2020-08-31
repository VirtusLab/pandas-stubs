import argparse
import re
import sys
from os import listdir, getcwd, walk
from os.path import join, splitext, isfile
from typing import List

from mypy.main import main as mypy_main

parser = argparse.ArgumentParser(description="Run Mypy over Pandas code-snippets")
parser.add_argument('patterns', type=str, nargs='*', help="Where to look for files")

PYTHON_VERSIONS = [(3, 6), (3, 7), (3, 8)]


def match(path: str, patterns: List[str]) -> bool:
    for pattern in patterns:
        if re.search(pattern, path):
            return True
    return False


def search_module(patterns: List[str], path: str) -> List[str]:
    for parent, _, module_files in walk(path):
        for file in sorted(module_files):
            name, extension = splitext(file)
            if extension in ['.pyi', '.py']:
                filename = join(parent, file)
                if match(filename, patterns):
                    yield filename


def run_mypy(patterns: List[str]) -> None:
    return_code = 0
    for major, minor in PYTHON_VERSIONS:
        root = getcwd()
        files = []
        ignore = {'__builtin__', '__pycache__', 'builtins', 'typing'}

        for name in listdir(root):
            full_name = join(root, name)
            prefix, extension = splitext(name)
            for filename in search_module(patterns, full_name):
                if prefix in ignore or prefix.startswith('.'):
                    continue
                ignore.add(prefix)
                files.append(filename)

        if len(files) == 0:
            print(f"# No input files! Exiting.")
            sys.exit(1)
        else:
            # Actually running Mypy
            flags = ['--python-version', f'{major}.{minor}', '--config-file', 'mypy.ini']
            print(f'# Running Mypy on {len(files)} files: {" ".join(flags)}')
            try:
                mypy_main('', sys.stdout, sys.stderr)
            except SystemExit as err:
                return_code = max(return_code, err.code)
    if return_code:
        print(f"# Finished with code {return_code}")
        sys.exit(return_code)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.patterns:
        run_mypy(args.patterns)
    else:
        print("Specify where to search for tests")
