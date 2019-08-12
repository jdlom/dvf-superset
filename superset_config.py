import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
POSTGRES_SUPERSER_DB = os.getenv('POSTGRES_SUPERSER_DB', 'superset')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'superset')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'superset')

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{username}:{password}@postgres:5432/{database}'.format(username=POSTGRES_USER,
                                                                                  password=POSTGRES_PASSWORD,
                                                                                  database=POSTGRES_SUPERSER_DB)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'
