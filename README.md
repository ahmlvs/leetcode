# leetcode

1. create env

```
python3 -m venv env
source env/bin/activate
```

2. install requirements

```
pip install -r requirements.txt
```

3. to test solution in folder "Some Problem"

with pytest

```
cd Some\ Problem
pytest -v
```

4. to test coverage and get html report

```
cd Some\ Problem
coverage run -m pytest
coverage html
```

and then open index.html in htmlcov. Or use report command

```
coverage report -m
```

to test branches (if, else, try, except etc.) use command

```
coverage run --branch -m pytest
```
