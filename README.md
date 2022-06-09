# Divar

A minimal clone of Divar. Divar is the largest Persian marketplace where you can sell and buy things. (Like craigslist)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages of the Project.

```bash
pip install -r requirements.txt
```

## Configuration
#### 1 - Create a config file with specefic name of local_config.py in root directory of the project. 
#### 2 - Add your local configurations in local_config.py.

```python
SECRET_KEY = ''

DB_NAME = ''
DB_USERNAME = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_PORT = 0000
```
## Usage
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)