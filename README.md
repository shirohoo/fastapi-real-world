![RealWorld Example Applications](media/realworld-dual-mode.png)

# Python 3.9 + Fast API 

## installation

First, you must have Python 3.9 installed on your machine and you just have to type the following commands into your shell in sequence.

```shell
$ git clone https://github.com/shirohoo/fastapi-real-world.git

$ cd fastapi-real-world

$ python -m venv .venv

$ source .venv/bin/activate

$ pip install -r requirements.txt

$ uvicorn application.main:app --reload
```