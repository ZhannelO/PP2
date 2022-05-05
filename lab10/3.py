import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5433,
    user='postgres',
    password='12345'
)

current = config.cursor()

try:
    user_id = input("Enter ID: ")
    to_change = input("What do you want to change?: ")
    data = input("To what value set the old value?: ")
    to_change = to_change.lower()
    """
        sql = '''
        UPDATE phonebook SET %s = %s WHERE id = %s;
    '''
    current.execute(sql, (to_change, data, user_id))
    """
    sql = '''
        UPDATE phonebook SET %s = %%s WHERE id = %%s;
    '''
    current.execute(sql % to_change, [data, user_id])
    config.commit()
except Exception as e:
    print(e.getMessage())

current.close()
config.close()