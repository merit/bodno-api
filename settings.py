from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

API_KEY = config('API_KEY', cast=Secret)
DATABASE_USER = config('DATABASE_USER', cast=str)
DATABASE_PASSWORD=config('DATABASE_PASSWORD', cast=Secret)
DATABASE_HOST=config('DATABASE_HOST', cast=str)
DATABASE=config('DATABASE', cast=str)
