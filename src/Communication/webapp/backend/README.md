# Backend of pet feeder

## Steps for setting up the project

Create a virtual environment in the root folder

```python
python3 -m venv venv
```

Active the virtual environment

```bash
source venv/bin/activate
```

Download dependencies

```python
pip install -r requirements.txt
```

## Steps for running the project

Active the virtual environment

```bash
source venv/bin/activate
```

Run the uvicorn server

```python
uvicorn main:app --reload
```

## Docs

You can visit the docs of the API on /docs. There you can test the server and view the endpoints
