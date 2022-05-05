#Implement deleting data from tables by username of phone
import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5433,
    user='postgres',
    password='12345'
)

current = config.cursor()
sql1 = '''
 DELETE FROM phonebook WHERE username=' Papa';
'''

current.execute(sql1)

current.close()
config.commit()
config.close()