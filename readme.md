# FAKEFLIX Web Application

## Description
A web application that demonstrates use of Python's Flask framework.

## Installation

**Installation via requirements.txt**
``` shell 
$ cd FakeFlix
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```
When using PyCharm, set the virtual environment using 'File -> Settings' and select 'Project:FakeFlix' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution
**Running the app**

From the *FakeFlix* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):
````shell
$ flask run
````

## Configuration

The *FakeFlix/.env* file contains variable settings. They are set with appropriate 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. te values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.

## Testing

Testing requires that file *FakeFlix/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *FakeFlix/tests/data* directory. 

E.g. 

`TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'Admin', 'PyCharmProjects', 'FakeFlix', 'tests', 'data')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):

`C:\Users\Admin\PyCharmProjects\FakeFlix\tests\data`

You can then run tests from within PyCharm.