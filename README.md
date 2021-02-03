**Create & Activate the virtual envrironment**

create virtual environment for blockchain-env

```
python -m venv blockchain-env
```

on windows

```
.\blockchain-env\Scripts\activate
```

on linux

```
sources blockchain-env/bin/activate
```

**Install all packages**

```
pip install -r requirements.txt
```

**Run the Tests**

Make sure to activate the virtual environment

```
python -m pytest tests
```
