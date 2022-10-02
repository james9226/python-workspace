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
    - name: Set up Python ${{ "3.10" }}
      uses: actions/setup-python@v3
    - name: Install dependencies
      run: |
        poetry installsss
    - name: Deploy docs
      run: |
        mkdocs build --clean
        mkdocs gh-deploy