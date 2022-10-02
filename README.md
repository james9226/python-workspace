# A Demo Repo for Python Code

https://james9226.github.io/python-workspace/

name: Python Workspace Doc Update
on:
  push:
    branches:
      - main
jobs:
  docupdate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
    - name: Install dependencies
      run: |
        poetry installsss
    - name: Deploy docs
      run: |
        mkdocs build --clean
        mkdocs gh-deploy

### TODO - add linter

          pip install flake8
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

### TODO - add cache
      - name: Cache Poetry deps
        uses: actions/setup-python@v3
        with:  # Restore cache, skip Python installation
          cache: poetry

sad