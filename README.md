# Divar
**A minimal clone of Divar. Divar is the largest Persian marketplace where you can sell and buy things. (Like craigslist)**

<p align="center">
  <img 
    width="400"
    height="400"
    src=".README_images/a4e3ee4b.png"
  >
</p>




## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages of the Project.

```bash
pip install -r requirements.txt
```

## Configuration


#### 2 - Add your local configurations in .env file.

```python
SECRET_KEY = ''

POSTGRES_DB = ''
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
DB_HOST = ''
```

## Usage

### run by docker
```
docker-compose up -d
```
### run without docker
```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)