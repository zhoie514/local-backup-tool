import os

# BASE_DIR = C:\\...\freebackup
BASE_DIR = os.path.split(os.path.dirname(__file__))[0]
db_file = os.path.join(BASE_DIR, 'data', 'database.sqlite')
sql_file = os.path.join(BASE_DIR, 'data', 'buildDatabase.sql')