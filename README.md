# A Demo Repo for Python Code
[![CI](https://github.com/james9226/python-workspace/actions/workflows/test.yaml/badge.svg)](https://github.com/james9226/python-workspace/actions/workflows/test.yaml)

https://james9226.github.io/python-workspace/
https://james9226-python-workspace-demo-gimqoe.streamlit.app/

### TODO - add linter

          pip install flake8
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
