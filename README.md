![RealWorld Example Applications](media/realworld-dual-mode.png)

# 🚀 Python 3.9 + Fast API 

## Installation

First, you must have the `Python 3.9` installed on your machine. if installed the Python 3.9 you just have to type the following commands into your terminal in sequence.

```shell
git clone https://github.com/shirohoo/fastapi-real-world.git
cd fastapi-real-world
python -m venv .venv
chmod +x .venv/bin/activate
source .venv/bin/activate
pip install -r requirements.txt
uvicorn application.main:app --reload
```

If you want to quit, you can send a shutdown signal to the operating system by typing `CTRL + C`. also you are in a `python virtual environment`, you will see the prompt `(venv)` in your terminal. you can type `deactivate` in your terminal to exit the python virtual environment. finally, you want to run a test, just type `pytest` into your terminal.