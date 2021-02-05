**Create & Activate the virtual envrironment**

create virtual environment for blockchain-env

```
python -m venv blockchain-env
```

on windows (cmd)

```
.\blockchain-env\Scripts\activate
```

on windows(git bash)

cd to Scripts folder in blockchain-env folder
then run

```
. activate
```

then cd back to top directory to work in virtual environment

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

**Run the Application and API on Default Port (5000)**

Make sure to activate the virtual environment

this will run app on default port 5000

```
python -m scripts.app
```

**Run the Application and API on PEER Port (random between 5001 - 6000)**

only can run under git bash cmd
open git bash command and activate virtual environment as per windows

```
export PEER=True
python -m scripts.app
```

will run app on different port than main app
