import os

# DB_USERNAME = os.environ.get('dbusername')
# DB_PASSWORD = os.environ.get('dbpassword')
# DB_NAME = os.environ.get('gothic_site')
# DB_HOST = os.environ.get('127.0.0.1')
# DB_PORT = os.environ.get('5432')

DB_USERNAME = "postgres"
DB_PASSWORD = "mysecretpassword"
DB_NAME = "postgres"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
