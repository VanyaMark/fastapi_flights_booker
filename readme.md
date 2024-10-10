1. Create a folder for this project
```
mkdir fastapi_flights_booker
cd fastapi_flights_booker
```

2. Create a virtual environment - this will mean that any dependencies that we create are isolated to this project
```
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```

3. Create a file called `requirements.txt` in the root folder and add the following dependencies:
```
fastapi
uvicorn
pydantic
```
These are the python packages that we will use to create the web server, fastapi will be our framework and uvicorn will be our XXX.

4. Now install the dependencies
```
pip install -r requirements.txt
```